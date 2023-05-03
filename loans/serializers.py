from rest_framework import serializers
from .models import Loans
from datetime import date, timedelta


class LoansSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Loans:
        
        return Loans.objects.create(**validated_data)
    
    def update(self, instance: Loans, validated_data: dict) -> Loans:
        validated_data = {
            "borrowed_date": date.today(),
            "devolution_date": date.today() + timedelta(days=1)
        }

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Loans
        fields= [
            "borrowed_date",
            "devolution_date",
            "is_devoluted",
            "copy_id"
            "user_id"
        ]
