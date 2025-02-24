from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from lab.models import Test
from lab.serializers import TestSerializer
import logging

logger = logging.getLogger('lab_api')

class TestView(APIView):
    def get(self, request, id=None):
        if id is None:
            tests = Test.objects.all()
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If id 
        try:
            test = get_object_or_404(Test, id=id)
            serializer = TestSerializer(test)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in get test:: {e}")
            return Response({"success":False, "message": "Test not found!"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            test = get_object_or_404(Test, id=id)
        except:
            return Response({"success":False, "message":"Test not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            test = get_object_or_404(Test, id=id)
        except:
            return Response({"success":False, "message":"Test not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TestSerializer(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            test = get_object_or_404(Test, id=id)
        except:
            return Response({"success":False, "message":"Test not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        test.delete()
        return Response({"success":True, "message":f"Id:{id} - Test deleted successfully!"}, status=status.HTTP_200_OK)
        
        
