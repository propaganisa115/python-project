from rest_framework import serializers
from ..models import Pembeli


class PembeliSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pembeli
		fields = '__all__'

