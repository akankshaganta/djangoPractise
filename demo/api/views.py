from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse,Http404
from app1.models import *
from .serializers import UserDataSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from employee.models import Employee

# Create your views here.
@api_view(['GET','POST'])
def students(request):
    if request.method == 'GET':
        data = UserData.objects.all()
        serializedData = UserDataSerializer(data, many=True)
        return Response(serializedData.data)
    
    elif request.method == 'POST':
        serializedData = UserDataSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
        else:
            return Response(serializedData.errors)

@api_view(['GET','PUT','PATCH','DELETE'])        
def updateUserDeatails(request,pk):
    try:
        student = UserData.objects.get(pk=pk)
    except UserData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialized = UserDataSerializer(student)
        return Response(serialized.data)
    
    elif request.method == 'PUT':
        serialized = UserDataSerializer(student,data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serialized = UserDataSerializer(student,data=request.data,partial=True)   
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serialized = EmployeeSerializer(employees, many=True)
        return Response(serialized.data, status= status.HTTP_200_OK)
    
    def post(self,request):
        serialized = EmployeeSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save() 
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeDetailView(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk) #returning the matched employee record
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        employee = self.get_object(pk)  #passing request pk to get_objects() and assigning the returned value/record to the employee variable
        serialized = EmployeeSerializer(employee)   #serializer converting python object to python dict datatype suitable for json
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        employee = self.get_object(pk)
        serialized = EmployeeSerializer(employee, data=request.data) #deserializer takes the request json data into data variable and converts the json data into python model instance
        if serialized.is_valid():   #checks the model basic validations for the converted model object
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status= status.HTTP_404_NOT_FOUND)