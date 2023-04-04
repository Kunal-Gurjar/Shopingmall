from django.urls import path
from . import views

urlpatterns = [
#Products
    path('products', views.ProductsView.as_view()),
    path('products/<str:pk>', views.ProductsList.as_view()),
#Category
    path('category', views.CategoryView.as_view()),
    path('category/<str:pk>', views.CategoryList.as_view()),

]