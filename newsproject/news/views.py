from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import ArticleForm
from django.views.generic import DetailView, ListView


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
            article = form.save()
            article.author = request.user
            article.save()
            return redirect('home')

    form = ArticleForm()

    data = {
        'title': 'Add article',
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def profile(request):
    # author = Author.objects.get()
    data = {
        'title': 'Profile'
    }
    return render(request, 'news/profile.html', data)


class ArticlesListView(ListView):
    model = Article
    template_name = 'news/all_articles.html'

    def get_queryset(self):
        return Article.objects.all().order_by("-time_create")


class ArticleDetailView(DetailView):
    model = Article


class AuthorDetailView(DetailView):
    model = Author
