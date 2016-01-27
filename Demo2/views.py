from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from Demo2.models import User, Account
from .serializers import AccountSerializer, UserSerializer


class signup(APIView):
    def post(self, request, format=None):
        data = request.data
        data["user"] = data
        print(data)
        accountSerializer = AccountSerializer(data=data)
        if User.objects.filter(mobile=data["mobile"]):
            return Response(status=status.HTTP_409_CONFLICT)
        elif accountSerializer.is_valid():
            accountSerializer.save()
            return Response(accountSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response(accountSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        a = Account.objects.get(token=str(request.auth))
        accountSerializer = AccountSerializer(a)
        return Response(accountSerializer.data, status=status.HTTP_200_OK)


class reset_password(APIView):
    def post(self, request, format=None):
        data = request.data
        account = Account.objects.get(user__mobile=data["mobile"])
        if account:
            accountSerializer = AccountSerializer(account, data=data)
            if accountSerializer.is_valid():
                accountSerializer.save()
                return Response(accountSerializer.data, status=status.HTTP_200_OK)
            else:
                return Response(accountSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
