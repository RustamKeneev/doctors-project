from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/',include('doctors.urls')),
    path('rest_auth/',include('rest_auth.urls')),
    path('rest_auth/registration/',include('rest_auth.registration.urls')),
]
