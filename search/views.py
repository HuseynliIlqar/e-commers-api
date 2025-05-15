from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from baskets.models import Product
from baskets.paginations import CustomPagination
from baskets.serializers import ProductSerializer


class ProductSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        search_query = request.query_params.get('search')

        if search_query:
            products = Product.objects.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )
        else:
            products = Product.objects.all()

        paginator = CustomPagination()
        page = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)