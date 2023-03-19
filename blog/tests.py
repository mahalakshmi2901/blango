from django.test import TestCase

# Create your tests here.
from models import Post, Comment
from django.contrib.auth.models import User
p = Post.objects.all()
u = User.objects.all()
print(p)