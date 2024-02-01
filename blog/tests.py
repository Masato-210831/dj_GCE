from django.test import TestCase
from .models import Article

class ArticleModelTests(TestCase):
  
  def test_validate_title(self):
    word_nums = 30 
    title = "a" * word_nums
    article = Article(title=title)
    self.assertIs(article.validate_title(), True)
    
  def test_validate_title_error(self):
    word_nums = 31 
    title = "a" * word_nums
    article = Article(title=title)
    self.assertIs(article.validate_title(), False)
