from django.shortcuts import render
from django.test import tag
from numpy import save
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account import serializers
from package.models import HolidayPackage, Review, Saved, Tag

from package.serializers import HolidayPackageSearchSerializer, HolidayPackageSerializer, HomeTagHolidayPackageSerializer, HomeTagsSerializer, ReviewSerializer, SavedSerializer
# Create your views here.


# to get tags for home screen
class HomeTagsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Tag.objects.all()
        serializer = HomeTagsSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# to get tags for home screen


class HomeTagHolidayPackagesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        queryset = HolidayPackage.objects.filter(tags=Tag.objects.get(id=id))
        serializer = HomeTagHolidayPackageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# to get holiday details for home screen


class HolidayPackagesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        queryset = HolidayPackage.objects.get(id=id)
        serializer = HolidayPackageSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

# to add and get review of a holiday package


class HolidayPackageReviewView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        reviews = Review.objects.filter(package_id=id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "failed to post review"}, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------SAVED
# to get saved package and add package
class SavedHolidayPackage(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, format=None):
        saved = Saved.objects.get(uid=id)
        serializer = SavedSerializer(saved)
        return Response(serializer.data, status=status.HTTP_200_OK)


# to add a holiday to saved
class AddSavedHolidayPackage(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, hid, format=None):
        saved = Saved.objects.get(uid=id)
        saved.holiday_package.add(hid)
        serializer = SavedSerializer(saved)
        return Response(serializer.data, status=status.HTTP_200_OK)

# to delete a holiday from saved


class RemoveSavedHolidayPackage(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id, hid, format=None):
        saved = Saved.objects.get(uid=id)
        saved.holiday_package.remove(hid)
        serializer = SavedSerializer(saved)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ----------------------------------------------------------------------------SEARCH
# to GET search recomendations


class SearchRecommendationsView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        package_locations = HolidayPackage.objects.values_list(
            'location', flat=True)
        package_country = HolidayPackage.objects.values_list(
            'country', flat=True)
        package_names = HolidayPackage.objects.values_list(
            'name', flat=True)
        return Response({
            "countries": package_country,
            "locations": package_locations,
            "name": package_names
        }, status=status.HTTP_200_OK)

# to GET search value


class SearchResultView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        key    = request.GET['key']
        packages_ids   = HolidayPackage.objects.values_list(
            'id', flat=True)
        # serializer = HolidayPackageSearchSerializer(packages, many=True)
        return Response({
            "Search_Result":packages_ids 
            },status=status.HTTP_200_OK)
    
    
