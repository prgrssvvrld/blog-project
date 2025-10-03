from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Тестовый заголовок",
            content="Тестовое содержимое"
        )

    def test_post_creation(self):
        """Проверка, что пост создаётся корректно"""
        self.assertEqual(self.post.title, "Тестовый заголовок")
        self.assertEqual(self.post.content, "Тестовое содержимое")
        self.assertTrue(self.post.created_at <= timezone.now())

    def test_post_str(self):
        """Проверка метода __str__"""
        self.assertEqual(str(self.post), "Тестовый заголовок")