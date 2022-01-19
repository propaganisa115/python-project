from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import PenjualSerializer
from ..models import Penjual
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError

class PenjualRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Penjual.objects.all()
    serializer_class = PenjualSerializer

class PenjualListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Penjual.objects.all()
    serializer_class = PenjualSerializer

class PenjualCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Penjual.objects.all()
    serializer_class = PenjualSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        if serializers.is_valid():
            if User.objects.filter(username=request.data['name']).exists():
                return Response(
                    {"detail": "Username already taken."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            response = super(PenjualCreateView, self).create(request, *args, **kwargs)
            user = User.objects.create(username=request.data['name'], email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            response.status = status.HTTP_200_OK
            response.data = {'token': request.data}
            return Response(serializers.data, status=status.HTTP_201_CREATED)