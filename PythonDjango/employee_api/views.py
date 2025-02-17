# employee_api/views.py
import logging
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger('employee_api')

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        logger.info(f"Creating new employee: {serializer.validated_data}")
        try:
            serializer.save()
            logger.info("Employee created successfully.")
        except Exception as e:
            logger.error(f"Error creating employee: {e}")
            raise e

    def get_queryset(self):
        logger.debug("Fetching list of employees.")
        return Employee.objects.all()

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_object(self):
        logger.debug("Fetching employee details.")
        try:
            return super().get_object()
        except Exception as e:
            logger.error(f"Error fetching employee: {e}")
            raise e