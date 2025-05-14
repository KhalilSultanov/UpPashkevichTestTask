from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


@extend_schema(tags=["Users"])
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
