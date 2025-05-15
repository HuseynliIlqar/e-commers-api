from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Basket, BasketItem
from .models import Product
from .serializers import BasketSerializer



class UserBasketAddView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            quantity = int(quantity)
            if quantity <= 0:
                return Response({"detail": "Quantity must be greater than 0."}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"detail": "Invalid quantity value."}, status=status.HTTP_400_BAD_REQUEST)

        basket = get_object_or_404(Basket, user=request.user)
        product = get_object_or_404(Product, id=product_id)

        basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
        if not created:
            basket_item.quantity += quantity
            basket_item.save()

        basket.total_price = sum(item.product.price * item.quantity for item in basket.items.all())
        basket.save()

        serializer = BasketSerializer(basket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserBasketDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        basket = get_object_or_404(Basket, user=request.user)
        serializer = BasketSerializer(basket)
        return Response(serializer.data)

class UserBasketItemUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        product_id = request.data.get('product_id')
        new_quantity = request.data.get('quantity')

        if not product_id or new_quantity is None:
            return Response({"detail": "Product ID and quantity are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_quantity = int(new_quantity)
        except ValueError:
            return Response({"detail": "Invalid quantity value."}, status=status.HTTP_400_BAD_REQUEST)

        basket = get_object_or_404(Basket, user=request.user)
        basket_item = get_object_or_404(BasketItem, basket=basket, product_id=product_id)

        if new_quantity <= 0:
            basket_item.delete()
            return Response({"detail": "Product removed from basket."}, status=status.HTTP_200_OK)

        basket_item.quantity = new_quantity
        basket_item.save()
        basket.total_price = sum(item.product.price * item.quantity for item in basket.items.all())
        basket.save()

        return Response({"detail": "Product quantity updated."}, status=status.HTTP_200_OK)

class UserBasketItemsDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        basket = get_object_or_404(Basket, user=request.user)
        deleted_count, _ = BasketItem.objects.filter(basket=basket).delete()

        if deleted_count == 0:
            return Response({"detail": "No items found in basket."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"detail": f"Deleted {deleted_count} items from your basket."}, status=status.HTTP_200_OK)
