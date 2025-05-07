from django.contrib.auth.models import Group, User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name', 'date_created', 'start', 'stop']

class AccelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccelData
        fields = ['id', 'name', 'date_created', 'x', 'y', 'z', 'board']

class GyroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GyroData
        fields = ['id', 'name', 'date_created', 'x', 'y', 'z', 'board']

class SpeedSerializer(serializers.ModelSerializer):
    trip = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.all()) 
    class Meta:
        model = SpeedData
        fields = ['id', 'trip', 'date', 'data']