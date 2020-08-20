from rest_framework import serializers
from .models import Post

# Irá converter nossos dados no formato JSON.

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at', 'update_at')

