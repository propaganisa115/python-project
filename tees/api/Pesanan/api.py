from django.db import connections
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import PesananSerializer,DetailPesananSerializer
from ..models import Pesanan, Detail_Pesanan
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError

class PesananListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer

class PesananDetailListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Detail_Pesanan.objects.all()
    serializer_class = DetailPesananSerializer

    def get_queryset(self):
        return Detail_Pesanan.objects.filter(id_pesanan=self.kwargs.get('pk'))

class PesananUpdateStatusView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        id = request.GET.get('id', None)
        status = request.GET.get('status', None)
        model = get_object_or_404(Pesanan, pk=id)
        data = {"status": status}
        serializer = PesananSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)