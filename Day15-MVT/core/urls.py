from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('paintings', views.painting_list, name='painting_list'),
    path('categories', views.category_list, name='category_list'),
    path('paintingShop/', views.home, name = 'home'),
    path('', RedirectView.as_view(url='/paintingShop', permanent=False)),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginview, name = 'login'),
    path('lgout/', views.logoutview, name = 'logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
