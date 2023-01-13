from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
  #? 2 tane permission metodu var, obj seviyesi olanı override ediyoruz.
  # def has_permission(self, request, view):                --> view seviyesi
  # def has_object_permission(self, request, view, obj):    --> object seviyesi
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or (obj.user == request.user))

