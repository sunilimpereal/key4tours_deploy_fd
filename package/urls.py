from django.contrib import admin
from django.urls import path, include
from account.serializers import SendPasswordResetEmailSerializer
from package.views import AddSavedHolidayPackage, HolidayPackageReviewView, HolidayPackagesView, HomeTagHolidayPackagesView, HomeTagsView, RemoveSavedHolidayPackage, SavedHolidayPackage, SearchRecommendationsView, SearchResultView
urlpatterns = [
    path('tags/', HomeTagsView.as_view(),name='tags'),
    path('tagHolidayPackages/<id>/', HomeTagHolidayPackagesView.as_view(),name='tagsHolidayPackage'),
    path('holidayPackages/<id>/', HolidayPackagesView.as_view(),name='holidayPackage'),
    path('holidayPackagesReview/<id>/', HolidayPackageReviewView.as_view(),name='holidayPackageReview'),
    path('holidayPackagesReview/', HolidayPackageReviewView.as_view(),name='holidayPackageReview'),
    #saved
    path('saved_holiday/<id>/', SavedHolidayPackage.as_view(),name='savedHoliday'),
    path('add_saved_holiday/<id>/<hid>/', AddSavedHolidayPackage.as_view(),name='add savedHoliday'),
    path('remove_saved_holiday/<id>/<hid>/', RemoveSavedHolidayPackage.as_view(),name='remove savedHoliday'),
    #search
    path('locations/', SearchRecommendationsView.as_view(),name='search recommendations'),
    path('search/', SearchResultView.as_view(),name='search result'),

]
