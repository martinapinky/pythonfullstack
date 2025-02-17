import logging
from rest_framework import serializers
from .models import Employee

logger = logging.getLogger('employee_api')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 
    
    def validate_salary(self, value):
        #Validate that the salary is a positive number
        if value <= 0:
            logger.error(f"Invalid salary value: {value}. Salary must be positive.")
            raise serializers.ValidationError("Salary must be a positive number.")
        return value