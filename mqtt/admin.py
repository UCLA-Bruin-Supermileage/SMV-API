import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import *

# Base admin class with CSV export functionality
class ExportCsvMixin:
    """
    Mixin that adds CSV export action to admin
    """
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta.verbose_name_plural}.csv'
        
        writer = csv.writer(response)
        writer.writerow(field_names)  # Write headers
        
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected to CSV"


# Admin classes with export functionality
class MessageHistoryAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("id", "topic", "date", "trip")
    actions = ["export_as_csv"]


class MQTTErrorAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("trip", "module", "event", "time", "error")
    actions = ["export_as_csv"]


class BoardDataAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("id", "date", "trip", "board", "data")
    actions = ["export_as_csv"]


class DataAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("id", "date", "trip", "data")
    actions = ["export_as_csv"]


class UIAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("id", "date", "trip", "type", "data")
    actions = ["export_as_csv"]


class BoardAxisAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("id", "date", "trip", "board", "axis", "data")
    actions = ["export_as_csv"]


class LocationAdmin(ExportCsvMixin, admin.ModelAdmin):
    list_display = ("id", "trip", "date", "latitude", "longitude")
    actions = ["export_as_csv"]


class TripAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ["export_as_csv"]


# Register your models here.
admin.site.register(MQTTError, MQTTErrorAdmin)
admin.site.register(HallVelocityData, DataAdmin)
admin.site.register(MotorTorqueData, DataAdmin)
admin.site.register(CurrentData, DataAdmin)
admin.site.register(BearBoardTempData, DataAdmin)
admin.site.register(MotorTempData, DataAdmin)
admin.site.register(UIData, UIAdmin) #1st paramter is imported from model.py
admin.site.register(GyroData, BoardAxisAdmin) #1st paramter is the model, 2nd parameter is the admin class what type of list data
admin.site.register(AccelData, BoardAxisAdmin) #2nd parameter is the admin class what type of list data
admin.site.register(PressureData, BoardDataAdmin)
admin.site.register(TorqueData, BoardDataAdmin)
admin.site.register(BrakeData, DataAdmin)
admin.site.register(GasData, DataAdmin)
admin.site.register(PowerData, BoardDataAdmin)
admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(SpeedData, DataAdmin) #18 total databases