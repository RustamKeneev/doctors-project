from rest_framework import serializers
from doctors.models import Doctors,DoctorType,MedicalStaffPositions

class DoctorDetailSerializer(serializers.ModelSerializer):
    doctor_type_name = serializers.SerializerMethodField()
    class Meta:
        model = Doctors
        fields = '__all__'

    def get_doctor_type_name(self,obj):
        if obj.doctorType:
            return obj.doctorType.name
        return None

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ('id','doctorFullName','doctorType','doctorWorkLocation')


class DoctorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorType
        fields = ('name','id')

class  MedicalStaffPositionsSerializer(serializers.ModelSerializer):
    # medical_staff_count = serializers.SerializerMethodField()
    class Meta:
        model = MedicalStaffPositions
        fields = ('name', 'id','medical_staff_count')
    #
    # def get_medical_staff_count(self,obj):
    #     return len(Doctors.objects.filter(medical_staff_positions=obj))