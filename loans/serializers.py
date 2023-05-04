from rest_framework import serializers
from .models import Loans

import ipdb

class LoansSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Loans:
        return Loans.objects.create(**validated_data)
    
    def update(self, instance: Loans, validated_data: dict) -> Loans:
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Loans
        fields= [
            "id",
            "borrowed_date",
            "devolution_date",
            "is_devoluted",
            "copy_id",
            "user_id",
        ]
