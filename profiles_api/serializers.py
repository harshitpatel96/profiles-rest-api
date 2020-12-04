from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        """We use meta class with ModelSerializer so 
        that it points to a specific model in our project """
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # set password to write only, cannot read
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        # default create function needs to be overriden so that we can modify how password is saved
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

        
