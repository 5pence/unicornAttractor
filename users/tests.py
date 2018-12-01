from django.test import TestCase, Client
from .models import User

# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        """This runs at start of test"""
        self.client = Client()

    def test_create_user(self):
        """This tests the user model"""
        u = User.objects.create(username='Fred', password='freddie')
        assert len(User.objects.all()) == 1

    def test_register_view(self):
        """This tests the register view page is correct"""
        res = self.client.get('/users/register/')
        assert b"<input" in res.content
        assert b"username" in res.content
        assert b"password1" in res.content
        assert b"password2" in res.content

    def test_register_mismatch_passwords(self):
        """This tests the business logic of entering a mismatched password on the registration form"""
        res = self.client.post('/users/register/', {'username': 'john', 'password1': 'smith', 'password2': 'smssith'})
        assert b"The two password fields didn&#39;t match." in res.content


    def test_register_sucess(self):
        """
        This tests the business logic of successfully registering
        which then redirects user
        """
        res = self.client.post('/users/register/', {'username': 'john', 'password1': 'smithsmith', 'password2': 'smithsmith'})
        # import pdb; pdb.set_trace()
        assert res.status_code == 302