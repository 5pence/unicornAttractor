from django.test import TestCase
from .models import User

# Create your tests here.
class TestUser(TestCase):
    def test_create_user(self):
        u = User.objects.create(username='Fred', password='freddie')
        assert len(User.objects.all()) == 1
