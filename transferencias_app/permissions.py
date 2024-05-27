from rest_framework import permissions


class IsTokenAuthenticated(permissions.BasePermission):
    """
    Custom permission to allow access to authenticated users with a valid token.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
