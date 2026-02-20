from django.urls import path
from . import views

app_name = 'insights'

urlpatterns = [
    # GET /insights (이미 만드신 목록 조회 뷰)
    # path('', views.insights_view, name='list'), 

    # DELETE /insights/{id}
    # <uuid:id>를 통해 URL에 들어온 ID 값을 views.insight_dismiss_view의 id 인자로 전달합니다.
    path('<uuid:id>/', views.insight_dismiss_view, name='dismiss'),
]