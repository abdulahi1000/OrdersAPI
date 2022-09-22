from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response 

from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field="id"

    print(queryset)

    def get_queryset(self):
        # userProfile = UserProfile.objects.get(user=self.request.user)
        return self.queryset.filter(email=self.request.user.email)

