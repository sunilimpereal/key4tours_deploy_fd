from django.contrib import admin

from package.models import Amenity, Day, HolidayPackage, Itinerary, Review, Saved, Tag

# Register your models here.
admin.site.register(HolidayPackage)
admin.site.register(Day)
admin.site.register(Itinerary)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Amenity)
admin.site.register(Saved)


# ⣿⣿⣿⣿⣿⣿⠏⠌⣾⣿⣿
# ⣿⣿⣿⣿⣿⠀⠀⠸⠿⣿⣿⣿
# ⣿⣿⣿⣿⠃⠀⣠⣾⣿⣿⣿
# ⣿⣿⡿⠃⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⣦⠀⠈⠻⣿⣿⣿
# ⣿⣿⠀⠀⠀⣿⣿⣿⠟⠉⠉⠉⢃⣤⠀⠈⢿⣿⣿⣿
# ⣿⣿⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⢹⣿⣧⠀⠀⠙⣿⣿
# ⣿⣿⡆⠀⠀⠈⠻⡅⠀⠀⠀⠀⣸⣿⠿⠇⠀⠀⢸⣿
# ⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠔⠛⠁⠀⠀⠀⣠⣿⣿
# ⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿
# ⣿⣿⣿⠃We Go Jim⠀⠀⣠⣾⣿⣿
# ⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿
# ⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿
# ⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
# ⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿
# ⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿
# ⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿
# ⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿