from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/<str:ct_model>/<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('search/', csrf_exempt(views.SearchResultsView.as_view()), name='search_results'),
    path('/contact', views.contact_page, name='contact_page'),
    path('/payment', views.payment_page, name='payment_page'),
    ]