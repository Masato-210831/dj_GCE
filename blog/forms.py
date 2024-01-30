from django import forms
from .models import Article

class ArticleCreateForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = {"body", "title"}
    # fields = {"title", "body"}
    