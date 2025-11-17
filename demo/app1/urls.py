from django.urls import path,include
from .views import *

app_name = 'app1'

urlpatterns = [
    # path('users/',toFetchUsers),
    # path('addUsers/',toPostUsers),

    #web application enpoint
    path('users/',toFetchAndPostUsersData),

    #api end point
    path('api/',include('api.urls')),
]