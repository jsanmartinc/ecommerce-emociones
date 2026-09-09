from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',  views.logout_view, name='logout'),
    path('products/create/', views.create_product, name='products_create'),
    path('products/edit/<int:product_id>/', views.edit_product, name='products_edit'),
    path('products/delete/<int:product_id>/', views.delete_product, name='products_delete'),
]