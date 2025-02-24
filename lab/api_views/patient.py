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
            patient = Patient.objects.get(id=id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.info(f"Error in get patiet:: {e}")
            return Response({"success":"false", "message": "Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        if patient is None:
            return Response({"success":"false", "message":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        if patient is None:
            return Response({"success":"false", "message":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        if patient is None:
            return Response({"success":"false", "message":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        patient.delete()
        return Response({"success":"true","message":f"Id:{id} - Patient deleted successfully!"}, status=status.HTTP_200_OK)
        
        
