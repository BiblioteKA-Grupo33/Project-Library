from rest_framework import serializers
from .models import Copy


class CopySerializer(serializers.ModelSerializer):

    class Meta:
        model = Copy
        fields = [
            "id",
            "book_id",
        ]

        extra_kwargs = {"book_id": {"read_only": True}}
