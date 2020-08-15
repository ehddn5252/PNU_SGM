from rest_framework import serializers
from .models import User,Stretagy,Result

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields ='__all__'


class stretagySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stretagy
        fields ='__all__'


class resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields ='__all__'