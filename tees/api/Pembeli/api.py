from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import PembeliSerializer
from ..models import Penjual,Pembeli, Keranjang
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError

class PembeliListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

class PembeliCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

class PembeliCreateView(generics.CreateAPIView):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        if serializers.is_valid():
            if User.objects.filter(username=request.data['name']).exists():
                return Response(
                    {"detail": "Username already taken."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            response = super(PembeliCreateView, self).create(request, *args, **kwargs)
            user = User.objects.create(username=request.data['name'], email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            response.status = status.HTTP_200_OK
            response.data = {'token': request.data}
            return Response(serializers.data, status=status.HTTP_201_CREATED)


class PembeliRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

