from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
from blog.models import Post

def index(request):
  posts = Post.objects.filter(title='hi everyone')
  print("-*-"*50)
  print(posts)
  # false

  return render(request, "blog/index.html", {"posts": posts})


