from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 인증 (auth 경로)
    path('login/', views.google_login_redirect, name='login'),
    path('callback/', views.google_callback, name='callback'),
    path('logout/', views.logout_view, name='logout'),

    # 프로필/설정 (user 경로)
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.setting_view, name='settings'),
]