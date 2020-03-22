from django.urls import path

from . import views 

urlpatterns = [
    path('products', views.getProducts, name ='list of product' ),
    path('test/', views.test, name ='test' ),
    
]