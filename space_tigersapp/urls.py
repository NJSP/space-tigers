from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
   path('', views.index),
   path('new', views.new),
   path('customers/', views.customer_list, name='customer_list'),
   path('customers/new', views.customer_new, name='customer_new'),
   path('customers/<int:id>/edit', views.customer_edit, name='customer_edit'),
   path('customers/<int:id>/delete', views.customer_delete, name='customer_delete'),
   path('<int:id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)