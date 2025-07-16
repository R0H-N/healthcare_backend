from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'address', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'contact', 'created_at']
        read_only_fields = ['created_at']


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'assigned_at']
        read_only_fields = ['assigned_at']
