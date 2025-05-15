from django.urls import path
from .views import (
    UserBasketAddView,
    UserBasketDetailView,
    UserBasketItemUpdateView,
    UserBasketItemsDeleteView
)

urlpatterns = [
    path('add/', UserBasketAddView.as_view(), name='basket-add'),
    path('detail/', UserBasketDetailView.as_view(), name='basket-detail'),
    path('item/update/', UserBasketItemUpdateView.as_view(), name='basket-item-update'),
    path('items/delete/', UserBasketItemsDeleteView.as_view(), name='basket-items-delete'),
]
