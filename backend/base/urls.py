from django.urls import path
from . import views


urlpatterns = [


    path('orders/', views.OrderListAPIView.as_view(), name='orders'),
    # path('orders/<int:id>/', views.OrderDetailsAPIView.as_view(), name='order'),


]
