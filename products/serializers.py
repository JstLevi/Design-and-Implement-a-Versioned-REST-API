from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "created_at"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must not be negative.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must not be below 0.")
        return value