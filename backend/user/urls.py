from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    # 브라우저에서 여기로 접속하면 로그인이 시작됩니다.
    path('google/login/', views.google_login_redirect, name='google-login-redirect'),
    # 구글이 인증 후 돌아오는 주소
    path('google/callback/', views.google_callback, name='google-callback'),

    # 기존 프로필 관련
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.setting_view, name='settings'),
]