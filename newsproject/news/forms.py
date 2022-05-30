from .models import Article
from django.forms import ModelForm, TextInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            })
        }

