"""
URL configuration for space_tigers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from space_tigersapp import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.views.generic.base import TemplateView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('space_tigersapp.urls')),
    path("", TemplateView.as_view(template_name="index.html"), name="index"), 
    path('customers/new', views.customer_new, name='customer_new'),  # Define a new customer view
    path('customers/', views.customer_list, name='customers'),  # Define a success view or page
    path('detail/',views.detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

