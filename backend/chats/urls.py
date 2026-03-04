from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # POST /chat/send - 메시지 전송(사용자 입력) 및 AI 응답 생성
    path('send', views.send_view, name='send'),

    # GET /chat/history - 대화 내역 조회
    path('history', views.history_view, name='history'),

    # GET /chat/suggestions - 추천 칩 조회
    path('suggestions', views.suggestions_view, name='suggestions'),
]
