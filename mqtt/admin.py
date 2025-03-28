from django.contrib import admin
from .models import *

#columns
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "date", "trip")
class MQTTErrorAdmin(admin.ModelAdmin):
    list_display = ("trip", "module", "event", "time", "error")
class BoardDataAdmin(admin.ModelAdmin):
    list_display = ("id","date", "trip", "board", "data")
class DataAdmin(admin.ModelAdmin):
    list_display = ("id","date", "trip", "data")
class UIAdmin(admin.ModelAdmin):
    list_display = ("id","date", "trip", "type", "data")
class BoardAxisAdmin(admin.ModelAdmin):
    list_display = ("id","date", "trip", "board", "axis", "data")
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "trip", "date", "latitude", "longitude")
# Register your models here.
admin.site.register(MQTTError, MQTTErrorAdmin)
admin.site.register(HallVelocityData, DataAdmin)
admin.site.register(MotorTorqueData, DataAdmin)
admin.site.register(CurrentData, DataAdmin)
admin.site.register(BearBoardTempData, DataAdmin)
admin.site.register(MotorTempData, DataAdmin)
admin.site.register(UIData, UIAdmin)
admin.site.register(GyroData, BoardAxisAdmin)
admin.site.register(AccelData, BoardAxisAdmin)
admin.site.register(PressureData, BoardDataAdmin)
admin.site.register(TorqueData, BoardDataAdmin)
admin.site.register(BrakeData, DataAdmin)
admin.site.register(GasData, DataAdmin)
admin.site.register(PowerData, BoardDataAdmin)
admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Trip)
admin.site.register(SpeedData, DataAdmin)

