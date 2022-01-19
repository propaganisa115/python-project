from rest_framework import serializers
from ..models import Kode_promo

class KodePromoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kode_promo
		fields = '__all__'