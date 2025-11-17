from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from app1.models import *
from .serializers import UserDataSerializer
from rest_framework.decorators import api_view
from rest_framework import status

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