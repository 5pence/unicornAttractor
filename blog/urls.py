from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blog/', views.post_list, name='post_list'),
]
