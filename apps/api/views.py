
from rest_framework import generics, filters
from apps.core.models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^subject']


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer