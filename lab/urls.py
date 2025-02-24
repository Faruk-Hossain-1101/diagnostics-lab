from django.urls import path
from lab.views import dashboard, patient_entry, get_child_test, add_referrer, add_patient_details
from lab.api_views.patient import PatientView
from lab.api_views.test import TestView
from lab.api_views.referral import ReferralView

urlpatterns = [
    path('', dashboard, name="index"),
    path('patient-entry/', patient_entry, name="patient_entry"),
    path('get-child-text/', get_child_test, name="get_child_test"),
    path('add-referrer/', add_referrer, name="add_referrer"),
    path('add-patient-details/', add_patient_details, name="add_patient_details"),

    ### API URLS
    # Patient
    path('api/patient/', PatientView.as_view(), name="patient"),
    path('api/patient/<int:id>', PatientView.as_view(), name="patient_with_id"),
    # Test
    path('api/test/', TestView.as_view(), name="test"),
    path('api/test/<int:id>', TestView.as_view(), name="test_with_id"),
    # Referral
    path('api/referral/', ReferralView.as_view(), name="referral"),
    path('api/referral/<int:id>', ReferralView.as_view(), name="referral_with_id"),
]