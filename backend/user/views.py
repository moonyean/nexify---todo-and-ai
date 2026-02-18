import os, requests, base64, json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# 1. 사용자를 구글 로그인 페이지로 리다이렉트
@api_view(['GET'])
@permission_classes([AllowAny])
def google_login_redirect(request):
    scope = "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")
    
    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}"
        f"&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline"
    )
    return redirect(auth_url)

# 2. 구글이 준 code를 받아서 처리하는 콜백 (가장 중요!)
@api_view(['GET'])
@permission_classes([AllowAny])
def google_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({"error": "Authorization code not provided"}, status=400)

    # A. 구글에 code를 주고 Access Token 받기
    token_endpoint = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "redirect_uri": os.getenv("GOOGLE_REDIRECT_URI"),
        "grant_type": "authorization_code",
    }
    
    token_res = requests.post(token_endpoint, data=token_data)
    access_token = token_res.json().get("access_token")

    # B. Access Token으로 구글 유저 정보 가져오기
    user_info_res = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_info = user_info_res.json()
    email = user_info.get("email")
    name = user_info.get("name")

    # C. DB에 유저 저장 또는 조회 (image_2493ff.png의 users 테이블 사용)
    user, created = User.objects.get_or_create(
        email=email,
        defaults={'username': email, 'name': name}
    )

    # D. Base64 토큰 생성 (요청하신 방식)
    payload = {
        "sub": email,
        "user_id": str(user.id),
        "name": user.name
    }
    token = base64.b64encode(json.dumps(payload).encode()).decode()

    return JsonResponse({
        "status": "success",
        "message": "Login successful",
        "token": token,
        "user": {
            "id": str(user.id),
            "email": user.email,
            "name": user.name
        }
    })

# 1. 프로필 조회 (GET /api/user/profile)
@api_view(['GET'])
# @permission_classes([IsAuthenticated]) # 인증 미들웨어 설정 후 주석 해제하세요.
def profile_view(request):
    """
    명세서: 이름, 이메일, 통계(Tasks Done, Streak) 조회
    """
    user = request.user
    
    # 인증되지 않은 사용자가 접근할 경우 (테스트용)
    if not user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    return JsonResponse({
        "status": "success",
        "data": {
            "name": user.name or user.username,
            "email": user.email,
            "stats": {
                "tasks_done": getattr(user, 'tasks_done', 0),
                "streak": getattr(user, 'streak', 0)
            }
        }
    })

# 2. 설정 변경 (PATCH /api/user/settings)
@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def setting_view(request):
    """
    명세서: Notifications, Dark Mode 토글 상태 및 이름 변경
    """
    user = request.user
    
    if not user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    try:
        # JSON 데이터 파싱
        data = json.loads(request.body)
        
        # 1. 이름 수정
        if 'name' in data:
            user.name = data['name']
            
        # 2. JSONB 필드(settings) 업데이트 (Notifications, Dark Mode 등)
        # 기존 설정 유지하며 업데이트
        current_settings = user.settings if user.settings else {}
        
        # 데이터가 있는 항목만 업데이트
        if 'notifications_enabled' in data:
            current_settings['notifications_enabled'] = data['notifications_enabled']
        if 'is_dark_mode' in data:
            current_settings['is_dark_mode'] = data['is_dark_mode']
            
        user.settings = current_settings
        user.save()

        return JsonResponse({
            "status": "success",
            "message": "Settings updated successfully",
            "data": {
                "name": user.name,
                "settings": user.settings
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)