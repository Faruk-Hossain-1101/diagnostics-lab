from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Patient
from .serializers import PatientSerializer

class PatientView(APIView):
    def get(self, request, id=None):
        if not id:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If id 
        patient = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        patient = self.get(id)
        if patient is None:
            return Response({"error":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        patient = self.get(id)
        if patient is None:
            return Response({"error":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        patient = self.get(id)
        if patient is None:
            return Response({"error":"Patient not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        patient.delete()
        return Response({"success":f"{patient.id} Patient deleted successfully!"}, status=status.HTTP_200_OK)
        
        
