from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item admin """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room admin"""

    pass


@admin.register(models.Photo)
class PhtoAdmin(admin.ModelAdmin):
    pass