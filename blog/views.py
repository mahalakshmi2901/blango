from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import CommentForm

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  print("post--", request.user, slug)
  if request.user.is_active:
    if request.method == "POST":
      print('if--')
      comment_form = CommentForm(request.POST)
      print('comment-form', comment_form)
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        return redirect(request.path_info)
    else:
      # print('else--')
      comment_form = CommentForm()
      # print('comment---', comment_form)
      
  else:
    # print('else else')
    comment_form = None
  # print('outside--', post, comment_form)
  return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )



