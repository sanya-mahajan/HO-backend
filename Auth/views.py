from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from rest_framework.authtoken.models import Token
#from rest_framework_simplejwt import RefreshToken

from . import serializers
User= get_user_model()


class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.UserRegisterationSerializer
    
    

    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        print(serializer)
    
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = serializer.save()

            user= User.objects.get(email= serializer.data['email'])
            token_obj,_= Token.objects.get_or_create(user=user)
            return Response({'message':"token generated",'payload':serializer.data,'token':token_obj.key}, status=status.HTTP_201_CREATED)

class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = serializers.CustomUserSerializer(user)
        #token = RefreshToken.for_user(user)
        data = serializer.data
        #data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        auth_token= Token.objects.get(user=user)
        data['token']= auth_token.key
        return Response(data, status=status.HTTP_200_OK)

class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserAPIView(APIView):
    """
    An endpoint to get all user details.
    """
    def get(self, request, format=None):
        users= User.objects.all()
        serializer_class = serializers.CustomUserSerializer
        userdata= serializer_class(users, many=True)
        return Response(userdata.data)
    
    

   