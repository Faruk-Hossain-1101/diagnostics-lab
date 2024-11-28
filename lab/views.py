from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from lab.models import Test, Referral, ReferralType

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
        
        return JsonResponse({"success":True, "data":""})

    