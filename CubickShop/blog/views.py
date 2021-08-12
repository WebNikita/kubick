from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Post

def all_news(request):
    posts = Post
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,)
    return render(request,'ctpo/news/detail.html',{'post': post})

# Create your views here.
