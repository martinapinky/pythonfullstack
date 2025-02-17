from django.contrib import admin
from django.urls import path
from .views import EmployeeListCreate, EmployeeDetail

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee-detail')
]
