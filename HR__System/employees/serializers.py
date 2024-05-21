from rest_framework import serializers
from .models import Employee,EmployeeToken


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'group')
        