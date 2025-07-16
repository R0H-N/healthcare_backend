from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorMappingViewSet,
    GetDoctorsByPatientView  
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'mappings', PatientDoctorMappingViewSet, basename='mappings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ Custom route to get doctors for a patient
    path('mappings/<int:patient_id>/', GetDoctorsByPatientView.as_view(), name='doctors-by-patient'),

    path('', include(router.urls)),
]
