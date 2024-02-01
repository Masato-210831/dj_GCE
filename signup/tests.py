from django.test import TestCase, Client
from .models import User

c = Client()

class UserModelTests(TestCase):
  email = "admin@gmail.com"
  password = "admin_"
  
  # 一時的に仮想dbとユーザー作成
  def setUp(self):
    User.objects.create_user(self.email, self.password)
    
  def test_user_login(self):
    resp = c.login(email=self.email, password=self.password)
    print("resp:", resp)
    self.assertIs(resp, True)
  
  def test_validate_email(self):
    domain = "@gmail.com"
    n = 255 - len(domain)
    email = "".join([
      "a" for _ in range(n)
    ]) + domain
    user = User(email=email)
    self.assertIs(user.validate_email(), True)
    
  def test_validate_email_error(self):
    domain = "@gmail.com"
    n = 256 - len(domain)
    email = "".join([
      "a" for _ in range(n)
    ]) + domain
    user = User(email=email)
    self.assertIs(user.validate_email(), False)
    
    
    