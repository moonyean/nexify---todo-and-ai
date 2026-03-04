"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from user import views as user_views

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to Nexify API',
        'endpoints': {
            'auth': {
                'login': 'POST /auth/login (Google OAuth)',
                'logout': 'POST /auth/logout',
            },
            'user': {
                'profile': 'GET /user/profile',
                'settings': 'PATCH /user/settings',
            },
            'tasks': 'GET /tasks/',
            'insights': 'GET /insights/',
            'chat': 'GET /chat/',
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    
    # 인증 관련
    # 아... 굳이 include를 쓸 필요없음. 사고를 유연하게.
    path('auth/login/', user_views.google_login_redirect, name='auth-login'),
    path('auth/callback/', user_views.google_callback, name='auth-callback'),
    path('auth/logout/', user_views.logout_view, name='auth-logout'),
    
    # 사용자 관련
    path('user/profile/', user_views.profile_view, name='user-profile'),
    path('user/settings/', user_views.setting_view, name='user-settings'),
    
    # 기타
    path('tasks/', include('tasks.urls')),
    path('insights/', include('aiinsights.urls')),
    path('chat/', include('chats.urls')),
]
