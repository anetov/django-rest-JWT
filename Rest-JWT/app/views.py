from django.shortcuts import render
from .models import Product, User
from rest_framework.viewsets import  ModelViewSet
from .serializer import ProductSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
