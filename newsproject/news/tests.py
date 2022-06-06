from django.test import TestCase
from news.models import *
from users.models import User


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        category = Category.objects.create()
        Article.objects.create(title='title', content='content', author=user, category=category)

    def test_title_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_author(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_category(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.get_absolute_url(), '/article/id=1')


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Author.objects.create(user=user, description='description')

    def test_user(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_description_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='name')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
