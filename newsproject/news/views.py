import asyncio
import logging

from asgiref.sync import sync_to_async
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from .models import *
from .forms import ArticleForm, ProfileUpdateForm

logger = logging.getLogger('main')


def index(request):
    articles = asyncio.run(get_all_articles_descending())
    context = {
        'title': 'PepegaNews',
        'articles': articles,
        'main': asyncio.run(get_article_by_id(50)),
        'first': asyncio.run(get_article_by_id(29)),
        'second': asyncio.run(get_article_by_id(35)),
        'third': asyncio.run(get_article_by_id(30)),
        'fourth': asyncio.run(get_article_by_id(28))
    }
    return render(request, 'news/index.html', context)


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            article.author = request.user
            article.save()
            return redirect('profile')

    form = ArticleForm()
    data = {
        'title': 'Add article',
        'form': form,
        'error': error
    }
    logger.info('Article created')
    return render(request, 'news/create.html', data)


class ProfileUpdateView(View):
    def get(self, request):
        author = asyncio.run(get_author_by_user_id(request.user))
        form = ProfileUpdateForm(instance=author)
        data = {
            "title": 'Update profile',
            "form": form
        }
        logger.info('Checked profile update')
        return render(request, 'news/profile_update.html', data)

    def post(self, request):
        author = asyncio.run(get_author_by_user_id(request.user))
        form = ProfileUpdateForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('profile')
        data = {
            "form": form
        }
        logger.info('Profile updated')
        return render(request, 'news/profile_update.html', data)


class ProfileView(View):
    def get(self, request):
        profile_articles = asyncio.run(get_filtered_ordered_articles_by_id(request.user))
        profile_user = asyncio.run(get_author_by_user_id(request.user))
        data = {
            'title': 'Profile',
            'profile_articles': profile_articles,
            'profile_user': profile_user
        }
        logger.info('Checked profile')
        return render(request, 'news/profile.html', data)


class ArticlesListView(ListView):
    model = Article
    template_name = 'news/all_articles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = asyncio.run(get_all_categories())
        context['title'] = 'All articles'
        context['article_list'] = asyncio.run(get_all_articles_descending())
        logger.info('Checked all articles')
        return context

    def get_queryset(self):
        return asyncio.run(get_all_articles_descending())


class FilteredArticlesView(View):
    def get(self, request, fltr):
        article_list = asyncio.run(get_filtered_articles_by_category(fltr))
        categories = asyncio.run(get_all_categories())
        context = {
            'title': fltr,
            'article_list': article_list,
            'categories': categories
        }
        logger.info('Checked filtered articles')
        return render(request, 'news/all_articles.html', context)


class ArticleDetailView(DetailView):
    model = Article
    logger.info('Checked article details')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm
    success_url = '/profile'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/profile'
    template_name = 'news/article_delete.html'


class AuthorView(View):
    def get(self, request, pk):
        author_user = asyncio.run(get_user_by_id(pk))
        author = asyncio.run(get_author_by_user_id(pk))
        author_articles = asyncio.run(get_filtered_ordered_articles_by_id(author.user))
        data = {
            'author_user': author_user,
            'author': author,
            'author_articles': author_articles
        }
        logger.info('Checked author details')
        return render(request, 'news/author_detail.html', data)


@sync_to_async
def get_all_articles_descending():
    articles = Article.objects.all().order_by("-time_create")
    return articles


@sync_to_async
def get_article_by_id(id):
    try:
        article = Article.objects.get(id=id)
        return article
    except:
        return None


@sync_to_async
def get_author_by_user_id(id):
    return Author.objects.get(user_id=id)


@sync_to_async
def get_filtered_ordered_articles_by_id(id):
    articles = Article.objects.filter(author=id).order_by("-time_create")
    return articles


@sync_to_async
def get_filtered_articles_by_category(id):
    return Article.objects.filter(category__name=id)


@sync_to_async
def get_all_categories():
    return Category.objects.all()


@sync_to_async
def get_user_by_id(id):
    return User.objects.get(pk=id)
