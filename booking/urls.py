from django.contrib import admin
from django.urls import path, include
from account.serializers import SendPasswordResetEmailSerializer
from booking.views import HolidayBookingView
from package.views import HolidayPackageReviewView, HolidayPackagesView, HomeTagHolidayPackagesView, HomeTagsView
urlpatterns = [
    path('holidayBookings/<uid>/', HolidayBookingView.as_view(),name='holidayBookings'),
 
   
   
    
]
