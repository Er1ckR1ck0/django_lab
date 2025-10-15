from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']
        labels = {
            'title': 'Введите заголовок статьи',
            'author': 'Введите автора статьи',
            'content': 'Введите контент',
        }
        widgets = {
            'content': forms.Textarea,
        }