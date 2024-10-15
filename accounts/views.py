from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404


    

class MyProfile(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if pk:
            profile_user = get_object_or_404(User, pk=pk)
        else:
            profile_user = request.user

        user_form = UserUpdateForm(instance=profile_user)
        profile_form = ProfileUpdateForm(instance=profile_user.profile)

        context = {
            'profile_user': profile_user,
            'user_form': user_form,
            'profile_form': profile_form,
            'is_owner': request.user == profile_user,
            'edit_mode': request.GET.get('edit', 'false') == 'true'
        }
        return render(request, 'accounts/profile.html', context)

    def post(self, request, pk=None):
        profile_user = request.user
        #if profile_user == request.user:
         #   profile_user = get_object_or_404(User, pk=pk) if pk else request.user
        #if request.user != profile_user:
         #   return redirect('profile', pk=profile_user.pk)

        user_form = UserUpdateForm(request.POST, instance=profile_user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')

        context = {
            'profile_user': profile_user,
            'user_form': user_form,
            'profile_form': profile_form,
            'is_owner': True,
            'edit_mode': True
        }
        return render(request, 'accounts/profile.html', context)
        
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_detail'

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return Profile.objects.get(user_id=user_id)
    
def ProfileDetailView2(request, pk):
    profile = Profile.objects.get(user_id=pk)
    is_owner = profile.user == request.user
    context = {
        'profile_detail': profile,
        'is_owner': is_owner, 
    }
    if is_owner:
        return redirect('profile')
    else:
        return render(request, 'accounts/profile.html', context)
        
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy("index")
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
class CustomerListView(LoginRequiredMixin, View):
    def get(self, request):
        profiles = Profile.objects.all()  # Query the Profile model
        context = {
            'profiles': profiles
        }
        return render(request, 'accounts/customers.html', context)
    