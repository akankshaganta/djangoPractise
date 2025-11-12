# from rest_framework import serializers
# from .models import UserData

# class UserDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserData
#         fields = '__all__'

from rest_framework import serializers
from .models import UserData

class UserDataSerializer(serializer.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'