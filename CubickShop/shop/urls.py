from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/<str:ct_model>/<str:slug>/', views.ProductDetailView.as_view(), name='detail'),
    ]