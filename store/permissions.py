from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.executor.user or request.user.is_superuser


class IsCreaterOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user or request.user.is_superuser
