import json
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from lab.models import Test, Referral, ReferralType, Patient, Appointment, AppointmentTest
import logging


logger = logging.getLogger('lab')


def dashboard(request):
    return render(request, 'lab/index.html')

def patient_entry(request):
    tests = Test.objects.all()
    referral_typs = ReferralType.objects.all()
    referrals = Referral.objects.all()
    context = {
        "tests": tests,
        "referrals": referrals,
        "referral_typs": referral_typs
    }
    return render(request, 'lab/patient_entry.html', context)


def get_child_test(request):
    if request.method == "POST":
        test_id = request.POST['test_id']
        child_test = Test.objects.filter(parent=test_id)
        data =[]
        for test in child_test:
            data.append({"id": test.test_id, "name": test.test_name, "price": test.price})

        return JsonResponse({"success":True,"data": data})


def add_referrer(request):
    if request.method == "POST":
        name = request.POST['name']
        type_id = request.POST['type_id']
        rate_value = request.POST['rate']

        referer = Referral(
            name=name,
            type_of_referral = ReferralType.objects.get(id=type_id),
            percentage = rate_value,
        )
        referer.save()
        data = {"id": referer.referral_id, "name":referer.name}
        return JsonResponse({"success":True, "data":data})
    
def add_patient_details(request):
    if request.method == "POST":    
        patient_data = {
            "first_name": request.POST.get('first_name'),
            "last_name": request.POST.get('last_name'),
            "phone": request.POST.get('phone'),
            "email": request.POST.get('email'),
            "address": request.POST.get('address'),
            "medical_history": request.POST.get('medical_history'),
            "gender": request.POST.get('gender'),
            "date_of_birth": request.POST.get('dob'),
        }

        doctor_id = request.POST['doctor']
        tests_dict = request.POST['tests']

        unique_apointment_id = str(uuid.uuid4()).split('-')[-1].upper()  
        india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        date = india_time.date()
        time = india_time.time().replace(microsecond=0)

        tests = json.loads(tests_dict)
        
        try:
            with transaction.atomic():
                patient = Patient(**patient_data)
                patient.save()

                referral = Referral.objects.get(id=doctor_id)
                appointment = Appointment.objects.create(
                    appointment_id = unique_apointment_id,
                    patient = patient,
                    referral = referral,
                    date = date,
                    time = time,
                    status = "Scheduled",
                )
                appointment.save()
                
                # Create Tests
                for test_id, test_details in tests.items():
                    test_name = test_details.get('name')
                    test_price = test_details.get('price')
                    
                    AppointmentTest.objects.create(
                        appointment=appointment,
                        test_name=test_name,
                        test_price=test_price
                    )

        except Exception as e: 
            logger.warning(f"Something went wrong::{e}")
            return JsonResponse({"success": False, "error": "An error occurred. Please try again later."})
        
        return JsonResponse({
            "success": True,
            "data": {"appointment_id": unique_apointment_id}
        })