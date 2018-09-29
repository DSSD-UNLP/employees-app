from employeesProject.employeesApp.models import Type, Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('firstname', 'surname', 'email', 'employeeType', 'id')

class EmployeeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('firstname', 'surname', 'email', 'employeeType','password', 'id')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'description', 'id')