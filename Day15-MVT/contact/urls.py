# urls.py in the contact app
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),  # Link to the contact form view
]
