from django.contrib import admin
from lab.models import Department, ReferralType, Patient, Test, Referral, Billing, Appointment, AppointmentTest

# Register Department model
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Department, DepartmentAdmin)

# Register ReferralType model
class ReferralTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ReferralType, ReferralTypeAdmin)

# Register Patients model with custom admin
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender',)
    readonly_fields = ('id',)

admin.site.register(Patient, PatientsAdmin)

# Register Tests model with custom admin
class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_name', 'department', 'price')
    search_fields = ('test_name', 'description')
    list_filter = ('department',)
    readonly_fields = ('id',)

admin.site.register(Test, TestsAdmin)

# Register Referrals model with custom admin
class ReferralsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_of_referral', 'percentage')
    search_fields = ('name', 'type_of_referral')
    list_filter = ('type_of_referral',)
    readonly_fields = ('id',)

admin.site.register(Referral, ReferralsAdmin)

# Register Billings model with custom admin
class BillingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'total_amount', 'final_amount', 'payment_status')
    search_fields = ('total_amount',)
    list_filter = ('payment_status',)
    readonly_fields = ('id',)

admin.site.register(Billing, BillingsAdmin)

# Register Appointments model with custom admin
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'referral_id', 'date', 'time', 'status')
    search_fields = ('status',)
    list_filter = ('status',)
    readonly_fields = ('id',)

admin.site.register(Appointment, AppointmentsAdmin)

# Register AppointmentTests model with custom admin
class AppointmentTestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_id', 'test_id', 'test_price')
    readonly_fields = ('id',)

admin.site.register(AppointmentTest, AppointmentTestsAdmin)

