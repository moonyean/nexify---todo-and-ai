from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessages
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import ChatMessages
import os
import json
from google import genai
from django.views.decorators.http import require_http_methods

# Create your views here.
def send_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    # parse JSON body or form data
    try:
        if request.content_type == 'application/json':
            payload = json.loads(request.body.decode('utf-8') or '{}')
        else:
            payload = request.POST.dict()
    except Exception:
        payload = {}

    user_content = payload.get('content')
    if not user_content:
        return JsonResponse({'status': 'error', 'message': 'content is required'}, status=400)

    user_msg = ChatMessages.objects.create(
        user=request.user,
        content=user_content,
        role='user'
    )

    # Generate AI response (best-effort, fall back on error message)
    try:
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_content
        )
        ai_content = getattr(response, 'text', str(response))
    except Exception:
        ai_content = '죄송해요, 답변을 생성하는 중에 문제가 발생했습니다.'

    ai_msg = ChatMessages.objects.create(
        user=request.user,
        role='ai',
        content=ai_content
    )

    return JsonResponse({
        'status': 'success',
        'user_message': {'role': 'user', 'content': user_msg.content, 'created_at': user_msg.created_at.isoformat()},
        'assistant_message': {'role': 'ai', 'content': ai_msg.content, 'created_at': ai_msg.created_at.isoformat()},
    })


def history_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    messages = ChatMessages.objects.filter(user=request.user).order_by('created_at')
    data = [
        {'role': m.role, 'content': m.content, 'created_at': m.created_at.isoformat()}
        for m in messages
    ]
    return JsonResponse({'status': 'success', 'history': data})


def suggestions_view(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    suggestions = [
        '내 하루 일정을 요약해줘',
        '지금 집중해야 할 작업 알려줘',
        '오늘 회의 요약해줘'
    ]
    return JsonResponse({'status': 'success', 'suggestions': suggestions})


# GET /chat/suggestions - 추천 칩 목록 반환
@require_http_methods(["GET"])
def suggestions_view(request):
    suggestions = [
        "Summarize my day",
        "Plan my focus time",
        "Create a tomorrow to-do list",
        "Summarize today",
        "Prioritize my tasks",
    ]
    return JsonResponse({"status": "success", "suggestions": suggestions})