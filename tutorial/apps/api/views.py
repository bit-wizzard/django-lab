from django.http import HttpResponse

from .models import Product, Category

def getProducts(req):
    products = Product.objects
    return HttpResponse("LOL")

def getProduct(req):
    pass

def getCategories(req):
    pass

def getCategory(req):
    pass

def getProductsByCategory(req):
    pass

def test(req):
    return HttpResponse("TEST LOL")