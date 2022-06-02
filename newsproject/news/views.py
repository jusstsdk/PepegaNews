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
    profile_articles = Article.objects.filter(author=request.user).order_by("-time_create")
    profile_user = Author.objects.get(user_id=request.user)
    data = {
        'title': 'Profile',
        'profile_articles': profile_articles,
        'profile_user': profile_user
    }
    return render(request, 'news/profile.html', data)


def edit_profile(request):
    data = {
        'title': 'Edit profile'
    }
    return render(request, 'news/edit_profile.html', data)


class ArticlesListView(ListView):
    model = Article
    template_name = 'news/all_articles.html'

    def get_queryset(self):
        return Article.objects.all().order_by("-time_create")


class ArticleDetailView(DetailView):
    model = Article


class AuthorView(View):
    def get(self, request, pk):
        author_user = User.objects.get(pk=pk)
        author = Author.objects.get(user_id=pk)
        author_articles = Article.objects.filter(author=author.user).order_by("-time_create")
        data = {
            'author_user': author_user,
            'author': author,
            'author_articles': author_articles
        }
        return render(request, 'news/author_detail.html', data)
