from django.contrib.auth.models import Group, User
from .models import Trip, Accel, SpeedData
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
        model = Accel
        fields = ['id', 'name', 'date_created', 'x', 'y', 'z']
class SpeedSerializer(serializers.ModelSerializer):
    trip = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.all())  # ✅ Use ID instead of URL
    class Meta:
        model = SpeedData
        fields = ['id', 'trip', 'date', 'data']