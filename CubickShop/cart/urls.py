from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<str:ct_model>/<str:slug>/', views.cart_add, name='cart_add'),
    # path('remove/<str:ct_model>/<str:slug>/', views.cart_remove, name='cart_remove'),
]