from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessages
import os
from google import genai

# Create your views here.
def send_view(request):
    if request.method == 'POST':
        user_content = request.data.get('content')
        
        user_msg = ChatMessages.objects.create(
            user=request.user,
            content=user_content,
            role='user'
        )

        try:
            client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=user_content
            )
            ai_content = response.text
        except Exception as e:
            ai_content = "죄송해요, 답변을 생성하는 중에 문제가 발생했습니다."

        ai_msg = ChatMessages.objects.create(
            user=request.user, role='ai', content=ai_content
        )

    return JsonResponse({
        "status": "success",
        "user_message": {"role": "user", "content": user_msg.content},
        "assistant_message": {"role": "ai", "content": ai_msg.content}
    })

def history_view(request):
    if request.method == 'GET':
        messages = ChatMessages.objects.filter(user=request.user)
        data = [
            {"role": m.role, "content": m.content, "created_at": m.created_at}
            for m in messages
        ]
        return JsonResponse({"status": "success", "history": data})


def suggestions_view(request):
    suggestions = [
        "내 하루 일정을 요약해줘",
    ]
    return JsonResponse({"status": "success", "suggestions": suggestions})