from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializers

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class=PostSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
    