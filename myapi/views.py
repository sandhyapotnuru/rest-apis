from rest_framework import viewsets

from myapi.serializers import UserSerializer
from myapi.models import User


class PersonViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
