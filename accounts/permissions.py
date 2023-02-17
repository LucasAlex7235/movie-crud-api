from rest_framework import permissions
from .models import Account
from rest_framework.views import Request, View
import ipdb


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Account):
        return request.user.is_employee or obj == request.user
