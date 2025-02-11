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
#set: DAQMessage
class SpeedData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Speed Data" 
class Location(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Location Data" 
#
# POWER DATA
#

class Temperature(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Temperature Data" 
class Gyro_x(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Gyro X" 
class Gyro_y(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Gyro Y" 
class Gyro_z(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Gyro Z" 
class Magnetometer(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Magnetometer" 
class Accel(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=0, null=0)
    y = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=0, null=0)
    z = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=0, null=0)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Acceleration Data" 
#set: steeringMessage
class Blinker(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   Blinkers" 

#set: motorMessage
class RPMData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    RPM Data" 
class Motor_StateData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Motor State Data" 
class CruiseData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Cruise Data" 
class M_Error_StatusData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    M Error Status Data" 
class ThrottleData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Throttle Data" 
class BrakeData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Brake Data" 

class Meter_CountData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Meter Count Data" 

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