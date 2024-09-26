from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Customer
from .forms import CustomerForm

# Create your views here.
def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products':Product_list})
    
def new(request):
    return HttpResponse('New Page')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_new(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def customer_edit(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})

def customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})
