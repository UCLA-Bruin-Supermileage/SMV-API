from django.contrib import admin
from .models import *

#columns
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "date", "trip")
class MQTTErrorAdmin(admin.ModelAdmin):
    list_display = ("trip", "module", "event", "time", "error")
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "trip", "date", "latitude", "longitude")
# Register your models here.
admin.site.register(MQTTError, MQTTErrorAdmin)
admin.site.register(HallVelocityData)
admin.site.register(MotorTorqueData)
admin.site.register(CurrentData)
admin.site.register(BearBoardTempData)
admin.site.register(MotorTempData)
admin.site.register(UIData)
admin.site.register(GyroData)
admin.site.register(AccelData)
admin.site.register(PressureData)
admin.site.register(TorqueData)
admin.site.register(BrakeData)
admin.site.register(GasData)
admin.site.register(PowerData)
admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Trip)
admin.site.register(SpeedData)

