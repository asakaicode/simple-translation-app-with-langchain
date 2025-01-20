from django.urls import path

from . import views

app_name = 'translation'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:translation_id>/', views.detail, name='detail')
]
