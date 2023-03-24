from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('phone/<int:id>/', views.index_detail, name='index_detail'),
]