from django.shortcuts import render
from django.shortcuts import render
from django.test import tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account import serializers
from booking.models import HolidayBooking
from booking.serializers import BookHolidayBookingSerializer, HolidayBookingSerializer
# Create your views here.


# to get holiday details for home screen
class HolidayBookingView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, uid, format=None):
        queryset = HolidayBooking.objects.filter(uid=uid)
        serializer = HolidayBookingSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, uid, format=None):
        serializer = BookHolidayBookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            holidayBooking = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
