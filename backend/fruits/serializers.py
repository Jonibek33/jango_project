from rest_framework import serializers
from .models import Fruits


class FruitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fruits
        fields = ['url', 'title', 'description', 'created_at', 'updated_at']