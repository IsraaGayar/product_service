from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import ListUserSerializer, MyTokenObtainPairSerializer, UserCreateUpdateSerializer
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    Provides CRUD operations.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [permissions.AllowAny]


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListUserSerializer
        else:
            return self.serializer_class


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer