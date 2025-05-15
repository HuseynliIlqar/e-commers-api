from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from baskets.models import Product
from baskets.paginations import CustomPagination
from baskets.serializers import ProductSerializer


class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        paginator = CustomPagination()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)