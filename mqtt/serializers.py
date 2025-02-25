from django.contrib.auth.models import Group, User
<<<<<<< HEAD
from .models import Trip
=======
from .models import Trip, Accel, SpeedData
>>>>>>> c785392ad1754da61cefe7d69140c77ee4d26a2b
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name', 'date_created', 'start', 'stop']
