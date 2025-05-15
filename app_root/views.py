from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        base_uri = request.build_absolute_uri
        return Response({

            'accounts': {
                'register': base_uri('/accounts/register/'),
                'login': base_uri('/accounts/login/'),
                'logout': base_uri('/accounts/logout/'),
                'password_change': base_uri('/accounts/password-change/'),
            },
            'baskets': {
                'user_detail': base_uri('/baskets/user/'),
                'item_update': base_uri('/baskets/item/update/'),
                'item_delete': base_uri('/baskets/item/delete/'),
            },
            'categories': {
                'list': base_uri('/categories/'),
                'detail': base_uri('/categories/{id}/'),
            },
            'products': {
                'list': base_uri('/products/'),
                'detail': base_uri('/products/{id}/'),
                'create': base_uri('/products/create/'),
                'update': base_uri('/products/{id}/update/'),
                'delete': base_uri('/products/{id}/delete/'),
            },
            'marketplace': {
                'list': base_uri('/marketplace/'),
                'detail': base_uri('/marketplace/{id}/'),
                'create': base_uri('/marketplace/create/'),
                'update': base_uri('/marketplace/{id}/update/'),
                'delete': base_uri('/marketplace/{id}/delete/'),
            },
            'search': {
                'products': base_uri('/search/products/'),
            }

        }, status=status.HTTP_200_OK)
