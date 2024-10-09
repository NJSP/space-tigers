from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.index),
   path('new', views.new),
   path('<int:id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)