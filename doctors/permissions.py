from rest_framework.permissions import BasePermission

from doctors.models import Doctors

class IsDoctorsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            doctors = Doctors.objects.get(pk=view.kwargs['pk'])
            return request.user == doctors.user_owner
