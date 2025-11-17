# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.http import HttpResponse,JsonResponse
# from .models import UserData
# from .serializers import UserDataSerializer

# # Create your views here.
# @api_view(['GET'])
# def toFetchUsers(request):
#     # data=list(UserData.objects.values())
#     data=UserData.objects.all()
#     serializer = UserDataSerializer(data,many = True)
#     print(data)

#     # return HttpResponse("hello world")
#     # return JsonResponse(data, safe=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def toPostUsers(request):
#     serializer = UserDataSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()   
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET','POST'])
def toFetchAndPostUsersData(request):
    if request.method == 'GET':
        data = UserData.objects.all()
        serializedData = UserDataSerializer(data, many= True)
        return Response(serializedData.data)
    
    elif request.method == 'POST':
        serializedData = UserDataSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data)
        else:
            return Response(serializedData.errors)
        
