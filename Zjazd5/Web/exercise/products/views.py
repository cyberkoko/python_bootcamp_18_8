from django.shortcuts import render,HttpResponse

# Create your views here.

from products.models import Product

def hello_world(request):
    return HttpResponse("Hello World")


def hello_world_name(request, name):
    return HttpResponse("Hello "+ name)

def products_list(request):
    products = Product.objects.all()
    output = ""
    for prod in products:
        output += str(prod) + "<br>"

    return HttpResponse(output)





#def products_detail(request, id):
#    products = Product.objects.get(pk=id)
#   output








