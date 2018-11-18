from django.test import TestCase
from blog.models import Post
from users.models import User

class TestBlog(TestCase):
    def test_create_post(self):
        u = User.objects.create(username='Fred', password='freddie')
        p = Post.objects.create(author=u, title='title', text='text')
        assert len(Post.objects.all()) == 1

