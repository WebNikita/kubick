from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<str:ct_model>/<str:slug>/<str:size>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('send_order/', views.send_order_to_the_email, name='send_order')
]