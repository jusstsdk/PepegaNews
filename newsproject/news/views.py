from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all().order_by("-time_create")
    return render(request, 'news/index.html', {'title': 'Home', 'articles': articles})


def about(request):
    return render(request, 'news/about.html', {'title': 'About'})


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid data'

    form = ArticleForm()

    data = {
        'title': 'Add article',
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
