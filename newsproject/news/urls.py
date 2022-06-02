from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('create', create, name='create'),
    path('profile', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('all-articles', ArticlesListView.as_view(), name='all_articles'),
    path('article-detail/id=<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('author/id=<int:pk>', AuthorView.as_view(http_method_names=['get']), name='author_detail'),
]
