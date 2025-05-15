from rest_framework import serializers
from .models import BasketItem, Basket, Product


class BasketItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = BasketItem
        fields = ['product_id', 'product_name', 'product_price', 'quantity']

class BasketSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    items = BasketItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Basket
        fields = ['user', 'items', 'total_price', 'id']

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username
        }

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    product_owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_name', 'product_owner']

    def get_category_name(self, obj):
        return [category.name for category in obj.category.all()]

    def get_product_owner(self, obj):
        return {
            "id": obj.product_owner.id,
            "username": obj.product_owner.username
        }
