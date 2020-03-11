from rest_framework import serializers
from core.models import UserModel, ProgressDetailModel

class ProgressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressDetailModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    progress = ProgressDetailSerializer(many=True)

    class Meta:
        model = UserModel
        fields = '__all__'

    