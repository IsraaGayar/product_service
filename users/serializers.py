from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.validators import URLValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    website = serializers.CharField(validators=[URLValidator()], required=False)
    bio = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = UserProfile
        fields = ('bio', 'website')

    def validate_bio(self, value):
        if len(value) < 50:
            raise serializers.ValidationError("Bio must be at least 50 characters long.")
        return value


class ListUserSerializer(serializers.ModelSerializer):
    """Serializer for the UserProfile model."""
    userprofile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email',
            'userprofile', 'is_staff', 'is_superuser')


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating User and UserProfile."""
    userprofile = UserProfileSerializer()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email',
            'userprofile', 'is_staff', 'is_superuser', 'userprofile', 'is_active', 'password')
        read_only_fields = ('id', 'is_staff', 'is_superuser')

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        password = validated_data.pop('password')
        user = UserSerializer().create(validated_data)
        user.set_password(password) 
        user.save()
        profile_data['user'] = user.id
        profile_serializer = CreateUserProfileSerializer(data=profile_data)
        profile_serializer.is_valid(raise_exception=True)
        profile = profile_serializer.save()
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        validated_data.pop('password', None)
        user = UserSerializer().update(instance, validated_data)
        if profile_data:
            profile_instance = instance.userprofile
            profile_serializer = UserProfileSerializer(profile_instance, data=profile_data, partial=True)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()
        return user



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT token claims."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        return token