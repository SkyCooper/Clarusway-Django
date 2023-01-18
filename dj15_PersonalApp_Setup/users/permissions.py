from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
  #? 2 tane permission metodu var, 
  #? her profil objesi içinden user'a bakıp, istek yapan user'a eşit mi? bu kontrol edilecek,
  #? bunun için  obj seviyesi olanı override ediyoruz.
  # def has_permission(self, request, view):                --> view seviyesi
  # def has_object_permission(self, request, view, obj):    --> object seviyesi
    
    def has_object_permission(self, request, view, obj):
                  # staff/admin ise       veya   kendisi yetki verilsin,
                  # True or True, True or False, False or True, --> hepsi TRUE döner
        return bool(request.user.is_staff or (obj.user == request.user))

