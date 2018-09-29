from django.shortcuts import render
from employeesProject.employeesApp.models import Employee, Type
from employeesProject.employeesApp.serializer import EmployeeSerializer, EmployeeLoginSerializer, TypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.pagination import PageNumberPagination
import code
from employeesProject.employeesApp.filter import EmployeeFilter,TypeFilter

class EmployeeList(APIView):
	
    def get(self, request):
        employees = EmployeeFilter(Employee.objects.all(), request).employees()
        paginator = PageNumberPagination()
        if request.GET.get('page_size') != None:
            paginator.page_size = request.GET.get('page_size')
        page = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_message={"status":"ok","message":"Created successfully","id":serializer.data['id']}
            return Response(response_message, status=status.HTTP_201_CREATED)
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
        serializer = EmployeeLoginSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_message = {"status":"ok", "message":"Updated successfully", "id":serializer.data['id']}
            return Response(response_message,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeLogin(APIView):
    def post(self,request):
        if (request.POST.get('email')) != None and (request.POST.get('password')) != None:
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                employee = Employee.objects.get(email=email)
            except:
                response_message = {"status":"error", "message":"Email not exists"}
                response_status = status.HTTP_404_NOT_FOUND
                return Response(response_message, status=response_status)
            if (employee.password == password):
                response_message = {"status":"ok", "message":"Valid user"}
                response_status = status.HTTP_200_OK
            else:
                response_message = {"status":"error", "message":"Invalid password"}
                response_status = status.HTTP_401_UNAUTHORIZED
            return Response(response_message, status=response_status)
        else:
            default_response = {"status":"error", "email":"This field is required.", "password":"This field is required."}
            return Response(default_response,status=status.HTTP_400_BAD_REQUEST)


class TypeList(APIView):

    def get(self, request):
        types = TypeFilter(Type.objects.all(),request).types()
        paginator = PageNumberPagination()
        if request.GET.get('page_size') != None:
            paginator.page_size = request.GET.get('page_size')
        page = paginator.paginate_queryset(types, request)
        serializer = TypeSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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


