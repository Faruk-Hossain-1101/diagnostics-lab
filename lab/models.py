from django.db import models


class TimestampedModel(models.Model):
    """Abstract base model to add created_at and updated_at timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(models.Model):
    """Lookup table for Test departments."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ReferralType(models.Model):
    """Lookup table for referral types."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Patient(TimestampedModel):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Test(TimestampedModel):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.test_name
    
class Referral(TimestampedModel):
    name = models.CharField(max_length=100)
    type_of_referral = models.ForeignKey(ReferralType, on_delete=models.PROTECT)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class Billing(TimestampedModel):
    BILL_TYPE_CHOICES = [('credit', 'Credit'), ('debit', 'Debit')]
    PAYMENT_STATUS_CHOICES = [('Paid', 'Paid'), ('Unpaid', 'Unpaid')]

    appointment = models.ForeignKey('Appointment', null=True, blank=True, on_delete=models.SET_NULL)
    bill_type = models.CharField(max_length=50, choices=BILL_TYPE_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Billing {self.id} - {self.payment_status}"

class PaymentDetail(TimestampedModel):
    PAYMENT_TYPE_CHOICES = [('Online', 'Online'), ('Cash', 'Cash'), ('Cheque', 'Cheque')]

    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE_CHOICES)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    cheque_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"PaymentDetail {self.id} - {self.payment_type}"


class Appointment(TimestampedModel):
    STATUS_CHOICES = [('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')]
    
    appointment_id = models.CharField(unique=True, max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.status}"

class AppointmentTest(TimestampedModel):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Test {self.test} for Appointment {self.appointment}"