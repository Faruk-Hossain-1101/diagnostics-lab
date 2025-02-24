from rest_framework import serializers
from lab.models import Patient, Test, Referral


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id','test_name', 'description', 'price', 'department', 'parent']

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ['id', 'name', 'address', 'department', 'type_of_referral', 'percentage']

 


