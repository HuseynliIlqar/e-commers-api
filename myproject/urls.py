from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_root.urls')),
    path('accounts/', include('accounts.urls')),
    path('baskets/', include('baskets.urls')),
    path('category/', include('category.urls')),
    path('products/', include('product.urls')),
    path('search/', include('search.urls')),
    path('filter/', include('filter.urls')),
    path('market_place/', include('market_place.urls')),

]
