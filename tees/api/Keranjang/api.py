from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import  KeranjangSerializer
from ..models import  Keranjang
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError


class KeranjangRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Keranjang.objects.all()
    serializer_class = KeranjangSerializer

class KeranjangListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Keranjang.objects.all()
    serializer_class = KeranjangSerializer

class KeranjangCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Keranjang.objects.all()
    serializer_class = KeranjangSerializer

class KeranjangByPembeliView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Keranjang.objects.all()
    serializer_class = KeranjangSerializer

    def get_queryset(self):
        return Keranjang.objects.filter(pembeli_id=self.kwargs.get('pk'))
