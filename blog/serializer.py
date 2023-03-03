from rest_framework import serializers
from .models import  Post
from users.models import User
   
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "email",
            "is_publisher",
        ]

# Post list serializer
class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = AuthorSerializer()
    
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "publisher",
            "title",
            "excerpt",
            "image_url",
            "thumbnail_url",
            "slug",
            "is_published",
            "created_at",
            "updated_at",
            "published_at"
            
        ]


# Post detail serializer
class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = AuthorSerializer()
    
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "publisher",
            "title",
            "excerpt",
            "body",
            "image_url",
            "slug",
            "created_at",
            "updated_at",
            "published_at"
            
        ]
        


# post create and update serializer
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "author",
            "id",
            "title",
            "body",
            "image",
            "slug",
            
        ]  
        
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        post.save()
        
        return post
        