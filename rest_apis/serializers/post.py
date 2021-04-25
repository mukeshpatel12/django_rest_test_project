
from post.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers
from ..serializers.user import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    author_id = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'liked', 'created_at', 'author_id')
        extra_kwargs = {
            'author_id': {'required': True}
        }

    def get_author(self, obj):
        return UserSerializer(obj.author).data

    def get_liked(self, obj):
        return UserSerializer(obj.liked.all(), many=True).data

    def create(self, validated_data):
        post = Post.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            author=User.objects.get(pk=validated_data['author_id']),
        )
        post.save()
        return post
