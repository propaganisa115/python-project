from rest_framework import serializers
from ..models import Keranjang


class KeranjangSerializer(serializers.ModelSerializer):
	class Meta:
		model = Keranjang
		fields = '__all__'