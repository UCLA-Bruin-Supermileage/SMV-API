from django.contrib.auth.models import Group, User
from .models import Trip, Accel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name', 'date_created', 'start', 'stop']

class AccelerometerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accel
        fields = ['id', 'trip', 'data', 'date']