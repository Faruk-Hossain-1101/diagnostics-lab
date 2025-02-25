from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from lab.models import Patient
from lab.serializers import PatientSerializer
import logging

logger = logging.getLogger('lab_api')

class PatientView(APIView):
    def get(self, request, id=None):
        if id is None:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If id 
        try:
            patient = get_object_or_404(Patient, id=id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in get patiet:: {e}")
            return Response({"success":False, "message": "Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            patient = get_object_or_404(Patient, id=id)
        except:
            return Response({"success":False, "message":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            patient = get_object_or_404(Patient, id=id)
        except:
            return Response({"success":False, "message":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            patient = get_object_or_404(Patient, id=id)
        except:
            return Response({"success":False, "message":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        patient.delete()
        return Response({"success":True, "message":f"Id:{id} - Patient deleted successfully!"}, status=status.HTTP_200_OK)
        
        
