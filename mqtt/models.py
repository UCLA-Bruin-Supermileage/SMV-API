from django.db import models
import sys
from datetime import datetime
sys.path.append("..")
# Create your models here.
    
class Trip(models.Model):
    name = models.CharField(max_length=128, default="", blank="", null="")
    active = models.BooleanField(default=False)
    date_created = models.DateField()
    start = models.DateTimeField()
    stop = models.DateTimeField( default=datetime.fromtimestamp(0), blank=datetime.fromtimestamp(0), null=datetime.fromtimestamp(0))

    def __str__(self):
        return f"{self.id}: {self.name}"
    
#
# Bear 1
#
class HallVelocityData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Bear 1: Hall Velocity Data" 
class MotorTorqueData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Bear 1: Torque Data" 
class CurrentData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Bear 1: Current Data" 
class BearBoardTempData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Bear 1: Board Temperature Data" 
class MotorTempData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Bear 1: Motor Temperature Data" 
#
# UI Data
#
class UIData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    type = models.CharField(max_length=64)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  UI: Data" 
#
# HS Data
#
class GyroData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    board = models.CharField(max_length=5, choices=[("HS1", "HS1"), ("HS2", "HS2"),("HS3","HS3"),("HS4","HS4")])
    axis = models.CharField(max_length=1, choices=[("x", "x"), ("y", "y"), ("z", "z")]) #x, y, z
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   HS: Gyro Data" 
class AccelData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    board = models.CharField(max_length=5, choices=[("HS1", "HS1"), ("HS2", "HS2"),("HS3","HS3"),("HS4","HS4")])
    axis = models.CharField(max_length=1, choices=[("x", "x"), ("y", "y"), ("z", "z")]) #x, y, z
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   HS: Accel Data" 
class PressureData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    board = models.CharField(max_length=5, choices=[("HS1", "HS1"), ("HS2", "HS2"),("HS3","HS3"),("HS4","HS4")])
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   HS: Pressure Data" 
class TorqueData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    board = models.CharField(max_length=5, choices=[("HS1", "HS1"), ("HS2", "HS2"),("HS3","HS3"),("HS4","HS4")])
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   HS: Torque Data" 
#
# FC Data
#
class BrakeData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    FC: Brake Data" 
class GasData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    FC: Gas Data" 
#
# Joulemeter Data
#
class PowerData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    board = models.CharField(max_length=7, choices=[("Joule_H", "Joule_H"), ("Joule_L", "Joule_L")])
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Joule: Power Data" 
#
# DAQ Message
#
class SpeedData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "     Speed Data" 
class Location(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "     Location Data" 


#extra data
class MessageHistory(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, default=None, blank=None)
    topic = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.topic
class MQTTError(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, default=None, blank=None)
    module = models.CharField(max_length=30, choices = (("mqtt", "mqtt"), ("ws", "ws")))
    event = models.CharField(max_length=30, choices = (("connect", "connect"), ("disconnect", "disconnect"), ("receive_message", "receive_message")))
    message = models.TextField()
    error = models.BooleanField()
    time = models.DateTimeField()