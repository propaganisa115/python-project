from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import ProductSerializer
from ..models import Product
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError

class ProductListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer