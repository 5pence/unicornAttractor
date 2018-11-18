from django.test import TestCase
from users.models import User
from tickets.models import Ticket
from .models import Transaction

class TransactionTest(TestCase):
    def test_transaction_create(self):
        u = User.objects.create(username='Fred', password='freddie')
        t = Ticket.objects.create(author=u, title='bug', text='big bug')
        tr = Transaction.objects.create(author=u, ticket=t, title='feature req', text='do this', amount=20)
        assert len(Transaction.objects.all()) == 1
