from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, LoanViewSet, GuarantorViewSet

router = DefaultRouter()
router.register(r'Client', ClientViewSet, basename='Client')
router.register(r'Loans', LoanViewSet, basename='loan')
router.register(r'Guarantors', GuarantorViewSet, basename='guarantor')

urlpatterns = [
    path('', include(router.urls)),
]
