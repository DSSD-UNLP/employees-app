from employeesProject.employeesApp.models import Employee, Type
from employeesProject.employeesApp.serializer import EmployeeSerializer, TypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from employeesProject.employeesApp.filter import EmployeeFilter,TypeFilter
from employeesProject.employeesApp.paginator_wrapper import StandardResultsSetPagination
from django.contrib.auth.hashers import check_password
import code

class EmployeeList(APIView):
	
    def get(self, request):
        employees  = EmployeeFilter(Employee.objects.all(), request).employees()
        paginator       = StandardResultsSetPagination()
        page = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        employee.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_message = {"status":"ok", "message":"Updated successfully", "id":serializer.data['id']}
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeLogin(APIView):
    def get(self,request,email):
        if (email != None):
            try:
                employee = Employee.objects.get(email = email)
            except Employee.DoesNotExist:
                response_message = {
                    "status":"error", 
                    "message":"Email not exists"
                }
                response_status = status.HTTP_404_NOT_FOUND

                return Response(response_message, status=response_status)

            response_message = EmployeeSerializer(employee).data
            response_message['status']='ok' 
            response_status = status.HTTP_200_OK
        else:
            response_message = {
                "status":"error", 
                "email":"This field is required."
            }
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response_message, status = response_status)


class TypeList(APIView):

    def get(self, request):
        types = TypeFilter(Type.objects.all(),request).types()
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(types, request)
        serializer = TypeSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = TypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeDetail(APIView):

    def get(self, request, pk):
        typeobject = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(typeobject)

        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        typeobject = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(typeobject)
        typeobject.delete()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        typeobject = get_object_or_404(Type,pk=pk)
        serializer = TypeSerializer(typeobject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
