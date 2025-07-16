from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    PatientSerializer, DoctorSerializer,
    PatientDoctorMappingSerializer, RegisterSerializer
)
from django.contrib.auth.models import User


# Registration API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Patient CRUD (only for authenticated users and filtered by creator)
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# Doctor CRUD (open to all authenticated users)
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


# Mapping between patients and doctors
class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
