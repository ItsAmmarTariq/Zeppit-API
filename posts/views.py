from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializers

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class=PostSerializers
    