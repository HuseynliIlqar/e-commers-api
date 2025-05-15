from django.urls import path
from .views import (MarketplaceAddView, MarketplaceDeleteView,
                    MarketplaceDetailView, MarketplaceListView, MarketPlaceplaceUpdateView)
urlpatterns = [
    path('list/', MarketplaceListView.as_view(), name='marketplace-list'),
    path('detail/<int:user_id>/', MarketplaceDetailView.as_view(), name='marketplace-detail'),
    path('add/', MarketplaceAddView.as_view(), name='marketplace-add'),
    path('update/<int:pk>/', MarketPlaceplaceUpdateView.as_view(), name='marketplace-update'),
    path('delete/<int:pk>/', MarketplaceDeleteView.as_view(), name='marketplace-delete'),
]