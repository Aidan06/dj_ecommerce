from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    GenericAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserAuthSerializer, UserCreateSerializer


class UserAuthAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class =UserAuthSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer.data.get('email'))
        except User.DoesNotExist:
            raise NotFound(detail='User not found')

        return Response({'token': user.auth_token.key})


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self, request, *args, **kwargs):
        self.serializer_class = UserSerializer
        super().get(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer
        super().post(request, *args, **kwargs)


class UserDetailDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

