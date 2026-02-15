"""
Django views and URL patterns – NO permission_classes.
Triggers: Agent 3 (Django class-based view detection, URL patterns).
"""

from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


# ──── Class-Based Views (Agent 3 detects APIView subclasses) ────

class CustomerViewSet(viewsets.ModelViewSet):
    """
    VIOLATION: ModelViewSet with NO permission_classes.
    Exposes all CRUD operations on customer PII (CRITICAL).
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve(self, request, pk=None):
        customer = self.get_object()
        return Response({
            'full_name': customer.full_name,
            'aadhaar_number': customer.aadhaar_number,
            'pan_card': customer.pan_card,
            'email': customer.email,
            'bank_account': customer.bank_account,
            'credit_card': customer.credit_card,
        })

    def list(self, request):
        customers = self.get_queryset()
        return Response([{
            'name': c.full_name,
            'aadhaar_number': c.aadhaar_number,
            'pan_card': c.pan_card,
            'passport': c.passport,
        } for c in customers])


class EmployeeAPIView(APIView):
    """
    VIOLATION: APIView with NO permission_classes / authentication_classes.
    Returns highly sensitive HR data (CRITICAL).
    """

    def get(self, request, emp_id):
        emp = Employee.objects.get(pk=emp_id)
        return Response({
            'aadhaar_number': emp.aadhaar_number,
            'pan_number': emp.pan_number,
            'bank_account': emp.bank_account,
            'epf_uan': emp.epf_uan,
            'esic': emp.esic,
            'credit_card': emp.credit_card,
        })

    def post(self, request):
        # Create employee with PII
        data = request.data
        emp = Employee.objects.create(
            aadhaar_number=data['aadhaar_number'],
            pan_number=data['pan_number'],
            bank_account=data['bank_account'],
        )
        return Response({'id': emp.id})


class PayrollView(APIView):
    """VIOLATION: No auth on payroll data (CRITICAL)."""

    def get(self, request, emp_id):
        payroll = Payroll.objects.filter(employee_id=emp_id)
        return Response([{
            'pan_number': p.pan_number,
            'epf_uan': p.epf_uan,
            'bank_account': p.bank_account,
            'net_salary': str(p.net_salary),
        } for p in payroll])


class KYCView(APIView):
    """VIOLATION: No auth on KYC documents (CRITICAL)."""

    def get(self, request, customer_id):
        kyc = KYCDocument.objects.filter(customer_id=customer_id)
        return Response([{
            'passport': k.passport,
            'voter_id': k.voter_id,
            'driving_license': k.driving_license,
            'aadhaar_number': k.aadhaar_number,
        } for k in kyc])


# ──── Django URL patterns (Agent 3 detects path() calls) ────

urlpatterns = [
    # VIOLATION: All these map to unprotected views with PII
    path('api/customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/employees/<int:emp_id>/', EmployeeAPIView.as_view()),
    path('api/employees/<int:emp_id>/payroll/', PayrollView.as_view()),
    path('api/customers/<int:customer_id>/kyc/', KYCView.as_view()),

    # LOW: No PII in handler
    path('api/products/', ProductListView.as_view()),
    path('api/health/', HealthCheckView.as_view()),
]
