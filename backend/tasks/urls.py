from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.tasks_view, name='tasks'),
    path('/<uuid:id>/done', views.is_done_view, name='is_done'),
    path('<uuid:id>/change_status', views.change_status_view, name='change_status'),
]