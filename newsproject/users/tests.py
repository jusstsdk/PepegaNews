from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='username')

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_title_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email address')

    def test_date_joined_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('date_joined').verbose_name
        self.assertEqual(field_label, 'date joined')
