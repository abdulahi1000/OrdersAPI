from rest_framework import serializers

from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
 
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password',
                  'first_name', 'last_name', 'phone_number']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should be only contain alphanumic character')

        return attrs

    def create(self, validated_data):
        print(validated_data)
        # user = User.objects.create(**validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=225, min_length=3)
    password = serializers.CharField(max_length=68, min_length=3, write_only=True)
    # tokens = serializers.SerializerMethodField(read_only=True)
    tokens = serializers.CharField(max_length=68,  read_only=True)
    first_name = serializers.CharField(max_length=68,  read_only=True)
    last_name = serializers.CharField(max_length=68,  read_only=True)
    username = serializers.CharField(max_length=68,  read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens',
                  'username', 'last_name', 'first_name']

       
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        return{
            'email':user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'tokens':user.tokens
        }


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=68, min_length=3, write_only=True)

    class Meta:
        model =User
        fields = ['email', 'password', 'tokens',
                  'username', 'last_name', 'first_name','phone_number'] 
   
