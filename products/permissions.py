
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ParseError, PermissionDenied


class CategoriesPermissions(permissions.BasePermission):
    """set Categories permission to allow anyone to list the categories to chose from,
        but only staff users or super users can create, edit or delete them"""

    def has_permission(self, request, view):
        user = request.user
        if view.action == 'list':
            return True
        elif user.is_authenticated and \
            (user.is_staff or user.is_superuser):
            return True
        return False


class ProductPermissions(permissions.BasePermission):
    """set products permission to allow anyone to list the products to choose from,
        but only staff users can create, or edit them, while only super users can delete them"""

    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        elif user.is_anonymous:
            return False
        elif user.is_superuser:
            return True
        elif user.is_staff and \
                not request.method == 'DELETE':
            return True
        return False
