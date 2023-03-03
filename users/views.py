from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from .serializers import UserCreateSerializer, UserProfileSerializer


class UserCreateView(APIView):
    permission_classes = [ permissions.AllowAny]
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response({"message": "account was created successfully"}, status=status.HTTP_201_CREATED)
            except Exception as exec:
                return Response({"msg":str(exec)})
            
        
        return Response(serializer.error)
            

class LoggedInUser(APIView):
    def get(self, request):
        try:
            user = User.objects.get(pk=request.user.id)
            
        except Exception as exec:
            return Response({"msg": str(exec)})
        serializer = UserProfileSerializer(user).data
        return Response(serializer, status=status.HTTP_200_OK)
        
        


