from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'author', 'title', 'text', 'created_date', 'published_date')

