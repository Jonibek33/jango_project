from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['url', 'title', 'discription', 'created_at', 'updated_at']