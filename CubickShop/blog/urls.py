from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_news, name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_detail, name='blog_detail'),
    
]