from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products':Product_list})
    
def new(request):
    return HttpResponse('New Page')

def detail(request, id):
    model_3d = get_object_or_404(Product, id=id)

    related_model_3d = Product.objects.exclude(id=id).order_by('?')[:3]
     
    return render(request, 'detail.html', {
        'model_3d': model_3d,
        'related_model_3d': related_model_3d,
        
    })

