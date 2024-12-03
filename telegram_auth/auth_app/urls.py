from django.urls import path, include
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_with_telegram, name='login_with_telegram'),
    path('telegram_login_callback/<str:token>/', views.telegram_login_callback, name='telegram_login_callback'),
]
