from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content']

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "content": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            }),
            "category": forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Category'
            })
        }
