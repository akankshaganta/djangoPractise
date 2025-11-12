from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from .models import UserData
from .serializers import UserDataSerializer

# Create your views here.
@api_view(['GET'])
def toFetchUsers(request):
    # data=list(UserData.objects.values())
    data=UserData.objects.all()
    serializer = UserDataSerializer(data,many = True)
    print(data)

    # return HttpResponse("hello world")
    # return JsonResponse(data, safe=False)
    return Response(serializer.data)

@api_view(['POST'])
def toPostUsers(request):
    serializer = UserDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
        return Response(serializer.data)
    else:
        return Response(serializer.errors)