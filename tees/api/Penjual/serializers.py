from rest_framework import serializers
from ..models import Penjual

class PenjualSerializer(serializers.ModelSerializer):
	class Meta:
		model = Penjual
		fields = '__all__'