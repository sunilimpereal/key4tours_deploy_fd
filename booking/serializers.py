
from rest_framework import serializers
from account.models import User
from account.serializers import UserProfileSerializer
from booking.models import HolidayBooking


class HolidayBookingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    @staticmethod
    def get_user(self):
        if self.id is None:
            return None
        # user = User.objects.get(id=)
        return UserProfileSerializer(self.uid).data

    class Meta:
        model = HolidayBooking
        fields = [
            'id',
            'number',
            'no_adult',
            'no_children',
            'package_id',
            'user',
            'uid',
            'payment_id',
            'start_date',
            'end_date',

        ]


class BookHolidayBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayBooking
        fields = [
            'id',
            'number',
            'no_adult',
            'no_children',
            'package_id',
            'uid',
            'payment_id',
            'start_date',
            'end_date',

        ]
