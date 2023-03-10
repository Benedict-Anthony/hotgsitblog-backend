from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import FormParser,MultiPartParser

from blog.permissions import ObjectPermision


from .serializer import PostCreateSerializer, PostListSerializer, PostDetailSerializer
from .models import Post


class PostView(APIView):
    def get(self, request, slug=None, related=None, **kwargs):
        if slug:
            try:
                queryset = Post.published.get(slug=slug)
                serializer = PostDetailSerializer(queryset).data
                return Response(serializer, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({"error":"data not found"}, status=status.HTTP_404_NOT_FOUND)
      
        queryset = Post.published.all()
        serializer = PostListSerializer(queryset, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    
    

class PostMutateView(APIView):
    permission_classes =[permissions.IsAuthenticated]
    parser_classes  =[FormParser,MultiPartParser]
  
    def get(self, request, slug=None, related=None, **kwargs):
        user = request.user
        id = kwargs.get("id")
        if id:
            try:
                queryset = Post.objects.get(id=id)
                serializer = PostDetailSerializer(queryset).data
                return Response(serializer, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({"message":"item not find in table"}, status=status.HTTP_404_NOT_FOUND)
        queryset = Post.objects.all().order_by("-created_at")
        serializer = PostListSerializer(queryset, many=True).data
        
        if request.user.is_publisher:
            serializer = PostListSerializer(queryset, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)
        
            
        qs = queryset.filter(is_published=True, author=user.id)
        serializer = PostListSerializer(qs, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def put(self, request, **kwargs):
        id = kwargs.get("id")
        if id:
            try:
                qs = Post.objects.get(pk=id)
                serializer = PostCreateSerializer(data=request.data ,instance=qs)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            except Post.DoesNotExist:
                return Response({"msg": "no such data in table"})
      
    
        return Response({"err": "something we wrong....."})
    
    def patch(self, request, id):
        qs = Post.objects.get(pk=id)
        if not request.user.is_publisher:
            return Response({"mesage":"You are not authorize to publish a post"}) 
        if qs.is_published:
            return Response({"msg":"Post has already be published"})
        
        qs.is_published = True
        qs.publisher = request.user
        qs.save()
        return Response({"msg":"published"},status=status.HTTP_206_PARTIAL_CONTENT)
    
    def delete(self, request, id, **kwargs):
        qs = Post.objects.get(pk=id)
        qs.delete()
        return Response({"msg": "Item was deleted"}, status=status.HTTP_202_ACCEPTED)
                
            
        
    
    
    
    
            
            
            
    
    
   
 
        
