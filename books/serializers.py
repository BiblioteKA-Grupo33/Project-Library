from rest_framework import serializers

from .models import Book

class BooksSerializer(serializers.ModelSerializer):
    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "category",
            "realese_date",
            "synopsis",
            "author",
            "quantity"
        ]
