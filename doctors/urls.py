from django.urls import path

from doctors.views import DoctorListView,DoctorView,DoctorTypeView,MedicalStaffView,MyDoctorsView

urlpatterns = [
    path('',DoctorListView.as_view()),
    path('my_doctors',MyDoctorsView.as_view({'get':'list'})),
    path('create',DoctorView.as_view({'post':'create'})),
    path('<int:pk>',DoctorView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('doctor_type',DoctorTypeView.as_view({'get':'list','post':'create'} )),
    path('doctor_type/<int:pk>',DoctorTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('medical_staff',MedicalStaffView.as_view({'get':'list','post':'create'})),
    path('medical_staff/<int:pk>',MedicalStaffView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]
