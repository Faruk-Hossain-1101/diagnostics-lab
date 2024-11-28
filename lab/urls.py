from django.urls import path
from .views import dashboard, patient_entry, get_child_test, add_referrer, add_patient_details
urlpatterns = [
    path('', dashboard, name="index"),
    path('patient-entry/', patient_entry, name="patient_entry"),
    path('get-child-text/', get_child_test, name="get_child_test"),
    path('add-referrer/', add_referrer, name="add_referrer"),
    path('add-patient-details/', add_patient_details, name="add_patient_details"),
]