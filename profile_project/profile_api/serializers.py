from rest_framework import serializers
from .models import UserProfile, Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileSerializer(serializers.ModelSerializer):
    profilePic = serializers.ImageField(
        max_length=None, use_url=True
    )
    class Meta:
        model = Profile
        fields = ('id', 'user_profile', 'phone', 'gender', 'profilePic', 'dateOfBirth', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
