from django.contrib.auth.models import Group, User
from .models import Trip, SpeedData, RPMData, MessageHistory, Accel, Magnetometer, Gyro_x, Gyro_y, Gyro_z
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name', 'date_created', 'start', 'stop']

class SpeedDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpeedData
        fields = ['trip', 'data', 'date']

class RPMDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RPMData
        fields = ['trip', 'data', 'date']

class AccelDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accel
        fields = ['trip', 'data', 'date']

class MagnometerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Magnetometer
        fields = ['trip', 'data', 'date']

class GyroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gyro_x
        fields = ['trip', 'data', 'date']