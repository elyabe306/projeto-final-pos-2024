from django.shortcuts import render
from rest_framework import viewsets
from .models import Users, Posts, Comments, Albums, Photos, Todos
from .serializers import UsersSerializer, PostsSerializer, CommentsSerializer, AlbumsSerializer, PhotosSerializer, TodosSerializer

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class PostsViewSet(viewsets.ModelViewSet):
   
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CommentsViewSet(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class AlbumsViewSet(viewsets.ModelViewSet):

    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

class PhotosViewSet(viewsets.ModelViewSet):

    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer

class TodosViewSet(viewsets.ModelViewSet):

    queryset = Todos.objects.all()
    serializer_class = TodosSerializer