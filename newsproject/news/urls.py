from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('create', create, name='create'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile_update'),
    path('all-articles', ArticlesListView.as_view(), name='all_articles'),
    path('article/id=<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/id=<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/id=<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('author/id=<int:pk>', AuthorView.as_view(http_method_names=['get']), name='author_detail'),
]
