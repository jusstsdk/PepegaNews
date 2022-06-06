from django.conf import settings
from django.db import models
from django.urls import reverse
from users.models import User
from cloudinary.models import CloudinaryField


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    content = models.TextField(blank=True)
    photo = CloudinaryField('imageURL')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
