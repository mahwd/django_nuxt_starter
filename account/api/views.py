from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from account.api.serializers import RegistrationSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_user_info(request):
    user = request.user
    if user:
        data = {
            "email": user.email,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "date_joined": user.date_joined,
            "is_admin": user.is_admin
        }
        return Response(data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def logout(request):
    user = request.user
    if user:
        user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
