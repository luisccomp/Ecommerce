from django.urls import path

from .views import LoginPageView, RegisterFormView

app_name = 'users'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterFormView.as_view(), name='register'),
]
