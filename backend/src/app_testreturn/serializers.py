from rest_framework import serializers
from .models import TestReturn

class TestReturnSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'

        model = TestReturn