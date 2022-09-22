from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/<int:id>', UserUpdateAPIView.as_view(), name='update'),
]
