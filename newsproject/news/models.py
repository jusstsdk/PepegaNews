from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
