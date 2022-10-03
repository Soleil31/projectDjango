from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
    path('type/', views.get_info_about_type),
    path('type/<str:element>/', views.get_info_about_one_type, name='horoscope-element'),
]
