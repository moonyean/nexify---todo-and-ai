from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # GET /tasks - 태스크 목록 조회
    path('', views.tasks_view, name='list'),
    
    # PATCH /tasks/{id}/done - 완료 상태 토글
    path('<uuid:id>/done', views.is_done_view, name='done'),
    
    # PATCH /tasks/{id} - 태스크 정보 수정
    path('<uuid:id>/', views.change_status_view, name='update'),
]