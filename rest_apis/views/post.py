from rest_framework import viewsets
from ..serializers.post import PostSerializer
from post.models import Post
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, permission_classes=[IsAuthenticated], methods=['post'])
    def likes(self, request):
        post = Post.objects.get(pk=request.data.get('blog_id'))
        if request.data.get('like_status') == 'like':
            post.liked.add(User.objects.get(pk=request.data.get('user_id')))
        elif request.data.get('like_status') == 'unlike':
            post.liked.remove(User.objects.get(pk=request.data.get('user_id')))
        return Response({"total_count": post.liked.all().count()})
