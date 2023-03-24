from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('mas_1/', views.mas_1, name='mas_1'),
    path('mas_2/', views.mas_2, name='mas_2'),
    path('mas_3/', views.mas_3, name='mas_3'),
    path('contact/', views.contact, name='contact'),
]