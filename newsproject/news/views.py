from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'title': 'Home', 'articles': articles})


def about(request):
    return render(request, 'news/about.html')
