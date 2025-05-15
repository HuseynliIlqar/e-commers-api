from django.urls import path
from .views import FilteredProductListView

urlpatterns = [
    path('', FilteredProductListView.as_view(), name='filtered_product_list'),
]