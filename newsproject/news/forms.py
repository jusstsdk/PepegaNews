from .models import *
from django import forms


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content', 'photo']

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "content": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            }),
        }
    category = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control'
        }),
        to_field_name="name"
    )
    photo = forms.ImageField(required=True)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['description']

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
