from django.urls import path
from .views import MyLoginView, RegisterView
from django.contrib.auth.views import LogoutView 
from .views import MyProfile, CustomerListView, ProfileDetailView2
from .views import ProfileDetailView
from . import views

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('profile/', MyProfile.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile2/<int:pk>/', views.ProfileDetailView2, name='profile2'),
    path('customers/', CustomerListView.as_view(), name='customers'),
]