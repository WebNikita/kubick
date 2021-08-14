from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Post

# class All_posts(DetailView):

#     model = Post
#     queryset = Post.objects.all()
#     template_name =  'blog.html'
#     print(Post)

def all_news(request):
    posts = Post.published.all()
    print(posts)
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year,
    publish__month=month,publish__day=day)
    return render(request,'blog_detail.html',{'post': post})

# Create your views here.
