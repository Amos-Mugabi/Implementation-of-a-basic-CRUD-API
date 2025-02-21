from rest_framework import generics
from .models import CustomerUser
from .serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer



