
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

from .models import UserProfile ,Project
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'profile_url', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            profile_url=validated_data.get('profile_url'),
            role=validated_data.get('role')
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        password = attrs.get('password')
        user = authenticate(request=self.context.get('request'), email=attrs.get('email'), password=password)

        if not user:
            raise serializers.ValidationError('No active account found with the given credentials')

        refresh = self.get_token(user)
        data = {'refresh': str(refresh), 'access': str(refresh.access_token)}

        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "name", "email", "password", "profile_url", "role"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": False},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "username", "email")
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'profile_url', 'role']


import logging
logger = logging.getLogger(__name__)


class UserProfileProjecSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'profile_url',]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = instance.id  # Ensure id is included
        return representation
class ProjectDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileProjecSerializer()
    members = UserProfileProjecSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'final_product', 'owner', 'members', 'table', 'picture_url']

    def update(self, instance, validated_data):
        # Extract nested fields
        print("Validated Data:", validated_data)
        owner_data = validated_data.pop('owner', None)
        members_data = validated_data.pop('members', [])

        # Update main instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Handle updating the owner
        if owner_data:
            owner_name = owner_data.get('name')
            if owner_name:
                try:
                    owner_instance = UserProfile.objects.get(name=owner_name)
                    instance.owner = owner_instance
                except UserProfile.DoesNotExist:
                    raise serializers.ValidationError({'owner': 'UserProfile with the given name does not exist'})

        # Handle updating members
        if members_data:
            print("Members Data:", members_data)
            members_instances = []
            for member_data in members_data:
                print("Processing Member Data:", member_data)
                member_name = member_data.get('name')
                print("Processing member_name:", member_name)
                if not member_name:
                    raise serializers.ValidationError({'members': 'Each member must have a name'})
                try:
                    member_instance = UserProfile.objects.get(name=member_name)
                    print("Found member instance:", member_instance)
                    members_instances.append(member_instance)
                except UserProfile.DoesNotExist:
                    raise serializers.ValidationError({'members': 'One or more UserProfiles with the given names do not exist'})
            instance.members.set(members_instances)

        instance.save()
        return instance

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        members_data = validated_data.pop('members', [])

        # Get or create the owner instance
        owner_instance, created = UserProfile.objects.get_or_create(**owner_data)

        # Create the project instance
        project_instance = Project.objects.create(owner=owner_instance, **validated_data)

        # Handle members
        for member_data in members_data:
            member_instance, created = UserProfile.objects.get_or_create(**member_data)
            project_instance.members.add(member_instance)

        return project_instance
class ProjectSerializer(serializers.ModelSerializer):
    owner = UserProfileProjecSerializer()
    members = UserProfileProjecSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'final_product', 'owner', 'members', 'picture_url']
