from django.test import TestCase
from users.models import User
from .models import Ticket


class TicketTest(TestCase):
    def test_ticket_create(self):
        u = User.objects.create(username='Fred', password='freddie')
        t = Ticket.objects.create(author=u, title='bug', text='big bug')
        assert len(Ticket.objects.all()) == 1


