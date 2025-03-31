from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.apis import TopExpensiveProductsByCategory
from products.views import ProductViewSet, CategoryViewSet
# from products.apis import ProductViewSet, CategoryViewSet
# from .views import TopExpensiveProductsByCategory, ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('top-expensive/', TopExpensiveProductsByCategory.as_view(), name='top-expensive'),
    path('', include(router.urls)),
]