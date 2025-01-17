from rest_framework import serializers
from .models import Users, Posts, Comments, Albums, Photos, Todos

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = "__all__"

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = "__all__"

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = "__all__"