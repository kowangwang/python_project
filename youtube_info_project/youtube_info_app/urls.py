from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_overview, name='show_overview'),
    path('get_video_desription/', views.show_overview, name='show_overview')
]