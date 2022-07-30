from rest_framework import serializers
from account.models import User
from account.serializers import UserProfileSerializer

from package.models import Amenity, Day, Duration, HolidayPackage, Itinerary, PriceCategory, Review, Saved, Tag


# get all tags
class HomeTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'description','show_on_home' ]


class HomeTagHolidayPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayPackage
        fields = ['id', 'name', 'description', 'image1']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = [
            'id',
            'day',
            'title',
            'subtitle1',
            'subtitle2',
            'description1',
            'description2',
            'image',
            'itinerary',
        ]

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = [
            'id',
            'name',
            'description',
            'icon',
        ]


class ItinerarySerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()
    amenities = AmenitiesSerializer(many=True, read_only=True)
    @staticmethod
    def get_days(self):
        if self.id is None:
            return None
        days = Day.objects.filter(itinerary=self)
        return DaySerializer(days, many=True).data

    class Meta:
        model = Itinerary
        fields = [
            'id',
            'name',
            'end_date',
            'start_date',
            'description',
            'inclusions',
            'exclusions',
            'amenities',
            'days'
        ]



class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    @staticmethod
    def get_user(self):
        if self.id is None:
            return None
        user = User.objects.get(id=self.uid)
        return UserProfileSerializer(user).data

    class Meta:
        model = Review
        fields = [
            'id',
            'uid',
            'title',
            'rating',
            'review',
            'createdAt',
            'package_id',
            'user'
        ]


class PriceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCategory
        fields = [
            'id',
            'dec_name',
            'title',
            'stars',
            'description',
            'one_adult',
            'two_adult',
            'three_adult',
            'child_add_price'
        ]


class DurationSerializer(serializers.ModelSerializer):
    PriceCategory = serializers.SerializerMethodField()
    itinerary = serializers.SerializerMethodField()

    @staticmethod
    def get_PriceCategory(self):
        if self.id is None:
            return None
        # itinerary = Itinerary.objects.get(id=self.itinerary)
        return PriceCategorySerializer(self.PriceCategory, many=True).data

    @staticmethod
    def get_itinerary(self):
        if self.id is None:
            return None
        # itinerary = Itinerary.objects.get(id=self.itinerary)
        return ItinerarySerializer(self.itinerary).data

    class Meta:
        model = Duration
        fields = [
            'id',
            'dec_name',
            'itinerary',
            'duration',
            'description',
            'PriceCategory',

        ]


class HolidayPackageSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    durations = serializers.SerializerMethodField()

    @staticmethod
    def get_durations(self):
        if self.id is None:
            return None
        # itinerary = Itinerary.objects.get(id=self.itinerary)
        return DurationSerializer(self.durations, many=True).data

    @staticmethod
    def get_reviews(self):
        if self.id is None:
            return None
        reviews = Review.objects.filter(package_id=self.id)
        return ReviewSerializer(reviews, many=True).data

    @staticmethod
    def get_tags(self):
        if self.id is None:
            return None
        # itinerary = Itinerary.objects.get(id=self.itinerary)
        return HomeTagsSerializer(self.tags, many=True).data

    class Meta:
        model = HolidayPackage
        fields = [
            'id',
            'name',
            'country',
            'location',
            'description',
            'durations',
            'tags',
            'about',
            'pdf',
            'is_active',
            'reviews',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'image6'
        ]


class HolidayPackageSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = HolidayPackage
        fields = [
            'id',
        ]


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = [
            'id',
            'uid',
            'holiday_package',
        ]
