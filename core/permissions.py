from rest_framework.permissions import BasePermission, IsAuthenticated


class IsSuperuser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsActive(BasePermission):
    """
    Allows access only to active users (is_active=True)
    """
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)


class IsActiveAuthenticated(IsAuthenticated, IsActive):
    def has_permission(self, request, view):
        return bool(
            IsAuthenticated.has_permission(self, request, view) and
            IsActive.has_permission(self, request, view)
        )