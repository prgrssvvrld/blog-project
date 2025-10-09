from django.test import TestCase,Client
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
class PostViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.post1 = Post.objects.create(title="Тест 1", content="Содержимое 1")
        self.post2 = Post.objects.create(title="Тест 2", content="Содержимое 2")

    def test_post_list_view_status(self):
        """Проверка, что страница /posts/ возвращает статус 200"""
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_content(self):
        """Проверка, что на странице отображаются заголовки постов"""
        response = self.client.get('/posts/')
        self.assertContains(response, "Тест 1")
        self.assertContains(response, "Тест 2")

    def test_post_detail_view_status(self):
        """Проверка, что страница детали поста возвращает статус 200"""
        response = self.client.get(f'/posts/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_content(self):
        """Проверка, что на странице детали поста отображается заголовок"""
        response = self.client.get(f'/posts/{self.post1.id}/')
        self.assertContains(response, "Тест 1")

def test_post_detail_view_not_found(self):
    """Проверка поведения при запросе несуществующего поста"""
    response = self.client.get('/posts/999/') 
    self.assertEqual(response.status_code, 404)