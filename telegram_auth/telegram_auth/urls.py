from django.urls import path, include

app_name = 'auth_app'

urlpatterns = [
    path('', include('auth_app.urls')),

]
