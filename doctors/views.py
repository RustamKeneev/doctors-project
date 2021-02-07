from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from doctors.models import Doctors, DoctorType, MedicalStaffPositions
from doctors.serializer import DoctorListSerializer, DoctorDetailSerializer, DoctorTypeSerializer, \
    MedicalStaffPositionsSerializer
from doctors.permissions import IsDoctorsOwner


class DoctorListView(ListAPIView):
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        staffMedical = self.request.query_params.get('medical_staff_positions')
        doctor_type = self.request.query_params.get('doctorType')
        filter_params = {}
        if staffMedical:
            filter_params.update({'staffMedical': staffMedical})
        if doctor_type:
            filter_params.update({'doctor_type': doctor_type})
        return Doctors.objects.filter(**filter_params)


class DoctorView(ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsDoctorsOwner]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        medical_staff_positions_id = serializer.data.get('medical_staff_positions')
        medical_staff_positions = MedicalStaffPositions.objects.get(id=medical_staff_positions_id)
        medical_staff_positions.medical_staff_count += 1
        medical_staff_positions.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user_owner != request.user:
            return Response('You cant', status=status.HTTP_403_FORBIDDEN)
        medical_staff_positions = instance.medical_staff_positions
        medical_staff_positions.medical_staff_count -= 1
        medical_staff_positions.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()






class DoctorTypeView(ModelViewSet):
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    lookup_field = 'pk'


class MedicalStaffView(ModelViewSet):
    queryset = MedicalStaffPositions.objects.all()
    serializer_class = MedicalStaffPositionsSerializer
    lookup_field = 'pk'


class MyDoctorsView(ModelViewSet):
    serializer_class = DoctorListSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        staffMedical = self.request.query_params.get('medical_staff_positions')
        doctor_type = self.request.query_params.get('doctorType')
        filter_params = {}
        if staffMedical:
            filter_params.update({'staffMedical': staffMedical})
        if doctor_type:
            filter_params.update({'doctor_type': doctor_type})
        return Doctors.objects.filter(user_owner=self.request.user, **filter_params)
