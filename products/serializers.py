from rest_framework import serializers
from .models import Product, Category
from django.utils.translation import gettext_lazy as _

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True)
    category_product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_id', 'price', 'description', 'created_at', 'modified_at', 'category_product_count']
        read_only_fields = ['created_at', 'modified_at', 'category']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(_("Price must be a non-negative number."))
        return value
