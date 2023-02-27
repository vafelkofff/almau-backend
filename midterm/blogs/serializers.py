from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_null=True)
    owner = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        blog = Blog(**validated_data)
        blog.save()
        return blog

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance