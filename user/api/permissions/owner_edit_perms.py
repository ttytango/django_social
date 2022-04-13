from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    edit_methods = ("PUT", "PATCH", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    # def has_object_permission(self, request, view, obj):
    #     if obj.user == request.user:
    #         return True

    def has_object_permission(self,request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.user == request.user
        else:
            return False
