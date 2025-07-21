from rest_framework import permissions


class IsOwnerOfVehicleOrRecord(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == user
        
        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            return obj.vehicle.owner and obj.vehicle.owner.user == user
        
        return False

# class IsOwnerOfVehicleOrRecord(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         # user = request.user
#         has_permissions = obj.owner.user == request.user
#         return has_permissions