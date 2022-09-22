from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from authentication.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,GenericAPIView,UpdateAPIView
# from requests import get


from .serializers import *

# Create your views here.


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class OrderDetailsAPIView(UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field="id"

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


