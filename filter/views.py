from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from baskets.models import Product
from baskets.paginations import CustomPagination
from baskets.serializers import ProductSerializer
from filter.filters import ProductFilter


class FilteredProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        qs = Product.objects.all()

        filt = ProductFilter(request.query_params, queryset=qs)
        if not filt.is_valid():
            return Response({'errors': filt.errors}, status=status.HTTP_400_BAD_REQUEST)
        qs = filt.qs

        term = request.query_params.get('search')
        if term:
            qs = qs.filter(
                Q(name__icontains=term) |
                Q(description__icontains=term)
            )

        order = request.query_params.get('ordering')
        allowed = ['price', '-price', 'created_at', '-created_at']
        if order in allowed:
            qs = qs.order_by(order)

        paginator = CustomPagination()
        page = paginator.paginate_queryset(qs, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)