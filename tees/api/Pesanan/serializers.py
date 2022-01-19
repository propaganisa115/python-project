from rest_framework import serializers
from ..models import Pesanan, Detail_Pesanan

class PesananSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pesanan
		fields = '__all__'

class DetailPesananSerializer(serializers.ModelSerializer):
	class Meta:
		model = Detail_Pesanan
		fields = '__all__'