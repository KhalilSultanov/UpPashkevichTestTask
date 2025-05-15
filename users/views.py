from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import UserModel
from .serializers import UserSerializer


@extend_schema(tags=["Users"])
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
