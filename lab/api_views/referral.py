from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from lab.models import Referral, Department, ReferralType
from lab.serializers import ReferralSerializer
import logging

logger = logging.getLogger('lab_api')


class ReferralView(APIView):
    def get(self, request, id=None):
        if id is None:
            referrals = Referral.objects.all()
            serializer = ReferralSerializer(referrals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            referral = get_object_or_404(Referral, id=id)
            serializer = ReferralSerializer(referral)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in Referral view:: {e}")
            return Response({"success":False, "message":"Referral not found!"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = ReferralSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            referral = get_object_or_404(Referral, id=id)
        except:
            return Response({"success":False, "message":"Referral not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReferralSerializer(referral, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id=None):
        try:
            referral = get_object_or_404(Referral, id=id)
        except:
            return Response({"success":False, "message":"Referral not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReferralSerializer(referral, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id=None):
        try:
            referral = get_object_or_404(Referral, id=id)
        except:
            return Response({"success":False, "message":"Referal not found!"}, status=status.HTTP_404_NOT_FOUND)

        referral.delete()
        return Response({"success":True, "message":f"Id-{id} deleted successfully!"})


