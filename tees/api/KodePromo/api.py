from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import KodePromoSerializer
from ..models import Kode_promo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError

class KodePromoListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Kode_promo.objects.all()
    serializer_class = KodePromoSerializer

class KodePromoCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Kode_promo.objects.all()
    serializer_class = KodePromoSerializer

class KodePromoRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Kode_promo.objects.all()
    serializer_class = KodePromoSerializer