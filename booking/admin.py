from django.contrib import admin

from booking.models import HolidayBooking, Person, Room

# Register your models here.
admin.site.register(HolidayBooking)
admin.site.register(Person)
admin.site.register(Room)
