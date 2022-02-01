from rest_framework import serializers
from home.models import Home
from posts.models import Post


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "image", "text", "created_at"]


class HomeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ["id", "title", "image", "floor", "floors", "price", "square", "tel", "created_at"]
