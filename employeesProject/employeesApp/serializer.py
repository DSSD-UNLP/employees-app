from employeesProject.employeesApp.models import Type, Employee
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model        = Employee
        fields       = ('firstname', 'surname', 'email', 'employeeType', 'id','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        employee = Employee(
            email        = validated_data['email'],
            firstname    = validated_data['firstname'],
            surname      = validated_data['surname'],
            employeeType = validated_data['employeeType'],
            password     = make_password(validated_data['password'])
        )
        employee.save()
        return employee

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'description', 'id')