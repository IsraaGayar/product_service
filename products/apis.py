from django.db.models import Count, OuterRef, Subquery, F
from rest_framework import generics, viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class TopExpensiveProductsByCategory(generics.ListAPIView):
    """
    API view to get the top 2 most expensive products in each category.
    """
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__id', 'category__name', 'price']  # Enable filtering
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Returns an optimized queryset to fetch top 2 expensive products per category,
        annotated with the total product count for each category.
        """
        category_counts = Category.objects.annotate(product_count=Count('products'))

        top_products_subquery = Product.objects.filter(
            category=OuterRef('category')
        ).order_by('-price')[:2]
        # ).order_by('-price')[:10]  #as for the low database objects, instead of 10 i changed it to 2 

        queryset = Product.objects.filter(
                category__isnull=False,
                pk__in=Subquery(top_products_subquery.values('pk'))
            ).annotate(
                category_product_count=Subquery(category_counts.filter(pk=OuterRef('category')).values('product_count'))
            ).filter(
                pk__in=Subquery(top_products_subquery.values('pk'))
            ).order_by('category__name', '-price').select_related('category')

        return queryset
