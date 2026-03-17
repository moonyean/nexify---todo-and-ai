# user/authentication.py
from rest_framework import authentication, exceptions
import base64, json
from .models import User

class CustomBase64Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # 1. 헤더에서 'Authorization: Bearer <토큰>' 가져오기
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        try:
            token = auth_header.split(' ')[1]
            # 2. Base64 풀어서 유저 정보 확인
            decoded_payload = base64.b64decode(token).decode('utf-8')
            payload = json.loads(decoded_payload)
            
            # 3. DB에서 유저 찾기
            user = User.objects.get(email=payload.get('sub'))
            return (user, None) # 인증 성공! (request.user에 유저가 담김)
        except Exception:
            raise exceptions.AuthenticationFailed('유효하지 않은 토큰입니다.')