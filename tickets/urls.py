"""Module for wiring up paths"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_ticket_list, name='ticket_list'),
    path('ticket_completed', views.post_ticket_completed, name='ticket_completed'),
    path('ticket_create', views.ticket_create, name='ticket_create'),
    path('vote', views.ticket_vote, name='ticket_vote'),
    path('ticket_single', views.ticket_single, name='ticket_single'),
    path('ticket_donation', views.ticket_donation, name='ticket_donation'),
    path('ticket_graphs', views.ticket_graphs, name='ticket_graphs'),

]
