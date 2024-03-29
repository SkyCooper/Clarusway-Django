from rest_framework import permissions

class IsStafforReadOnly(permissions.IsAdminUser):
    message = 'You do not have permission perform this action.'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
        # if request.method = 'GET':  # sadece böylede yazılabilir.
            return True
        return bool(request.user and request.user.is_staff)

# custom permission tanımlarken neye izin vereceğini anlatan bir isim vermek gerekli,
# IsAdminUser'dan customize edeceğimiz için onu import edip inherit ettik
# Bütün permission'lar True/False döner, yani istek yapanın yetkisi varsa True döner ve izin verir.
# Burada GET için True döner, ve her tür kullanıcı GET yapar,
# GET harici bir istek gelirse False olur ve yapmadan aşağıya geçer,
# O zamanda sadece staff ise yani admin ise True döner.

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') demektir.

class IsOwnerAndStaffOrReadOnly(permissions.BasePermission):
    
    # def has_permission(self, request, view):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user.is_staff and (obj.create_user == request.user))
        
