from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('edit/<slug:slug>/<int:product_id>/', views.edit_product, name='edit_product'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
