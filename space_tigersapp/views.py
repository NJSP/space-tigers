from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Customer
from .forms import CustomerForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


# Automatically make a new user using the information from the CustomerForm
class UserCreateView(CreateView):
    template_name = 'signup.html'
    form_class = UserForm
    success_url = reverse_lazy('success')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def detail(request, id):
    model_3d = get_object_or_404(Product, id=id)

    related_model_3d = Product.objects.exclude(id=id).order_by('?')[:3]
     
    return render(request, 'detail.html', {
        'model_3d': model_3d,
        'related_model_3d': related_model_3d,
        
    })