"""testing module for the tickets app"""
from django.test import TestCase
from users.models import User
from .models import Ticket


class TicketTest(TestCase):
    """Testing class for tickets"""

    def test_ticket_create(self):
        """Testing fuction for ticket creation form"""
        user_name = User.objects.create(username='Fred', password='freddie')
        ticket = Ticket.objects.create(author=user_name, title='bug', text='big bug')
        assert len(Ticket.objects.all()) == 1
