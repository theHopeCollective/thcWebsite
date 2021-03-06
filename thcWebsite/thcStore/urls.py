from django.urls import path
from . import views

app_name = 'thcStore'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_create/', views.product_create.as_view(), name='product_create'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
