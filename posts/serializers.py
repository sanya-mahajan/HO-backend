from rest_framework import serializers
from .profanitycheck import profanity_check
from .models import Category, Comment, Post

class CategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"

    
    def get_categories(self, obj):
        categories = list(
            cat.name for cat in obj.categories.get_queryset().only("name")
        )
        return categories

    def get_likes(self, obj):
        likes = list(
            like.username for like in obj.likes.get_queryset().only("username")
        )
        return likes

class PostWriteSerializer(serializers.ModelSerializer):
    #author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #write Post body field as censored content

    def validate_body(self, value):
        print("value",value)
        if profanity_check(value):
            raise serializers.ValidationError("Profanity is not allowed")
        return value
    
    class Meta:
        model = Post
        fields = "__all__"

class CommentReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

class CommentWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = "__all__"