"""
Employee HR models – triggers PII model field discovery.
"""

from django.db import models


class Employee(models.Model):
    """HR Employee model with sensitive PII."""
    employee_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    aadhaar_number = models.CharField(max_length=12)
    pan_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=11)
    epf_uan = models.CharField(max_length=12)
    esic = models.CharField(max_length=17)
    credit_card = models.CharField(max_length=20, blank=True)
    passport = models.CharField(max_length=10, blank=True)
    voter_id = models.CharField(max_length=10, blank=True)
    driving_license = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hr_employees'


class Dependent(models.Model):
    """Employee dependent – may contain children's data."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dependent_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    aadhaar_number = models.CharField(max_length=12, blank=True)
    is_minor = models.BooleanField(default=False)
    guardian_name = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'hr_dependents'


class Payroll(models.Model):
    """Monthly payroll record."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=7)
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2)
    pan_number = models.CharField(max_length=10)
    epf_uan = models.CharField(max_length=12)
    esic = models.CharField(max_length=17)
    bank_account = models.CharField(max_length=20)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'hr_payroll'
