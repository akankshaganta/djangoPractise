from django.urls import path
from .views import *

app_name='api'

urlpatterns=[
    path('students/',students),
    path('students/<int:pk>/',updateUserDeatails)
]