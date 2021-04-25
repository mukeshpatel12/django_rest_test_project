from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# from ..serializers import UserSerializer, UserSerializerReadOnly
from ..serializers.user import UserSerializer

"""
    priority: To perform CRUD operation on model User
    purpose: Provides list and detail view of User
"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserSerializer

