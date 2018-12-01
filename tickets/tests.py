"""testing module for the tickets app"""
from django.test import TestCase, Client
from users.models import User
from .models import Ticket, Vote


class TicketTest(TestCase):
    """Testing class for tickets"""

    def setUp(self):
        """This runs at start of test, creates a user and a ticket"""
        self.client = Client()
        # set up something to vote on
        user = User.objects.create(username='Fred', password='freddie')
        self.ticket = Ticket.objects.create(author=user, title='bug', text='big bug', ticket_type='bug')
        res = self.client.post('/users/register/', {'username': 'voter', 'password1': 'votevote', 'password2': 'votevote'})

    def test_ticket_model_create(self):
        """Testing function for ticket creation form"""
        user_name = User.objects.create(username='Fred2', password='freddie')
        ticket = Ticket.objects.create(author=user_name, title='feature', text='big feature')
        assert len(Ticket.objects.all()) == 2

    def test_ticket_view(self):
        """This checks the tickets view page has loaded correctly"""
        res = self.client.get('/tickets/')
        assert b'big bug' in res.content
        assert b'have this too' in res.content

    def test_ticket_vote_view(self):
        """
        This test checks that the user has already voted for a ticket
        and therefore cannot vote again
        """
        res = self.client.get('/tickets/vote?id={}&next=/tickets/'.format(self.ticket.id))
        assert res.status_code == 302
        res = self.client.get('/tickets/')
        assert b'you voted, thanks' in res.content

    def test_ticket_create_view(self):
        """This test checks the creat ticket view"""
        res = self.client.get('/tickets/ticket_create')
        assert b'<input type="text" name="title"' in res.content
        assert b'<textarea name="text"' in res.content

    def test_ticket_create_validation_failed(self):
        """This ticket checks the validation process and message by entering an empty ticket"""
        res = self.client.post('/tickets/ticket_create', {'title': '', 'text': ''})
        assert b'This field is required' in res.content

    def test_ticket_create_success(self):
        """This tests that upon a ticket being added successfully it is redirected to the ticket page"""
        res = self.client.post('/tickets/ticket_create', {'title': 'my new bug', 'text': 'bug goes here'})
        assert res.status_code == 302
        res = self.client.get('/tickets/')
        assert b'my new bug' in res.content

    def test_graph_page(self):
        """
        This test creates two users and one ticket which they both vote on.
        The test checks that the graph page shows that the highest bug has 2 votes
        """
        user1 = User.objects.create(username='Fred10', password='freddie')
        ticket = Ticket.objects.create(author=user1, title='bug', text='big bug', ticket_type='bug')
        user2 = User.objects.create(username='Fred11', password='freddie')
        vote1 = Vote(user=user1, ticket=ticket)
        vote1.save()
        vote2 = Vote(user=user2, ticket=ticket)
        vote2.save()
        res = self.client.get('/tickets/ticket_graphs')
        assert b'2 votes' in res.content
