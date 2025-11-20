from django.urls import path
from .views import *

app_name='api'

urlpatterns=[
    path('students/',students),
    path('students/<int:pk>/',updateUserDeatails),
    path('employees/',Employees.as_view()),
    path('employees/<int:pk>/',EmployeeDetailView.as_view()),
]