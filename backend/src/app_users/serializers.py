from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = '__all__'
        fields = (
            'username',
            'password'
        )

        model = Users