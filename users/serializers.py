from rest_framework import serializers

from users.models import User

# creeating a user serializer
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        
        if len(password) <=4:
            raise ValueError("password is too short")
        
        user = User.objects.create(**validated_data)
        user.is_active = True
        user.set_password(password)
        
        user.save()
        return user
    
#user profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_publisher",
            
        ]
        
