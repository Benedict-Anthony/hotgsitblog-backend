from rest_framework.permissions import BasePermission


class ObjectPermision(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_publisher:
            return True
        
        return request.user == obj.user