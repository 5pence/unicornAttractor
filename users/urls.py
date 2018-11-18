from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path('register/', views.register, name='users_register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users_logout')
]


