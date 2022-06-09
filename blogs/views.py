from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render
from django.test import tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account import serializers
from blogs.models import Blog, Tag
from blogs.serializers import BlogSerializer
from booking.serializers import HolidayBookingSerializer
# Create your views here.



#view blog detail 
class BlogDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        queryset = Blog.objects.get(id=id)
        serializer = BlogSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


#view blog detail 
class TagBasedBlogsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request,tag, format=None):
        queryset = Blog.objects.filter(tag = Tag.objects.get(name=tag))
        serializer = BlogSerializer(queryset,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    