from rest_framework import serializers
from .models import Follow


class FollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "user_id", "book_id"]
