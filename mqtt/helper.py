import random
from paho.mqtt import client as mqtt_client
from .models import Trip, MQTTError
from datetime import datetime
from .topics import topics_list as topics
import os
import sys
from random import randint
# import logging

import time

sys.path.append('..')
from smvDashboard.settings import ip_address_mqtt as ip_address


# logger = logging.getLogger(__name__)

LOCATION = [0,0,0]

broker = ip_address
port = 1883
global CLIENT
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'smv'
password = os.environ.get("MQTT_PW")

def connect_mqtt(client_id=client_id) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            MQTTError.objects.create(module='mqtt', event='connect', message='connected', error=False, time=datetime.now(), trip=Trip.objects.last())
        else:
            #error state
            MQTTError.objects.create(module='mqtt', event='connect', message=f"Failed to connect, return code {rc}, client: {client}\n", error=True, time=datetime.now(), trip=Trip.objects.last())
            return None
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def store(msg):
    try:
        #1. Compare msg value. Is it in bounds of min/max?
        payload = round(abs(float(msg.payload.decode())), 3) #absolute value of input, rounded to 3 decimal places
        # print(f"{msg.topic}: {payload}")
        if round(float(msg.payload.decode()), 3) > 999.000 or round(float(msg.payload.decode()), 3) < 0:
            #if out of bounds(needs to be [0, 999.000))
            payload =  round(float(msg.payload.decode()), 3)
            MQTTError.objects.create(module='mqtt', event='receive', message=f'Invalid Argument {msg.payload.decode()}', error=True, time=datetime.now(), trip=Trip.objects.last())
        
        else:
            #error is false unless specifically set          
            MQTTError.objects.create(module='mqtt', event='receive', message=f'{payload}', error=False, time=datetime.now(), trip=Trip.objects.last())
            #update associated model
            if "Gyro" in msg.topic or "Accel" in msg.topic:
                topics[msg.topic]['model'].objects.create(date=datetime.now(), data=payload, trip=Trip.objects.last(), board=topics[msg.topic]['board'], axis=topics[msg.topic]['axis']) 
            elif msg.topic in ["/HS1/Torque_HS", "/HS2/Torque_HS","/HS3/Torque_HS","/HS4/Torque_HS","/HS1/Pressure", "/HS2/Pressure","/HS3/Pressure","/HS4/Pressure","/Joule_L/Power", "/Joule_H/Power"]:
                topics[msg.topic]['model'].objects.create(date=datetime.now(), data=payload, trip=Trip.objects.last(), board=topics[msg.topic]['board']) 
            else:
                topics[msg.topic]['model'].objects.create(date=datetime.now(), data=payload, trip=Trip.objects.last()) 
            if str(msg.topic) == "/DAQ/Latitude" and str(msg.topic) == "/DAQ/Longitude":
                #do NOT deal with long/lat here. need to implement separate feature to store it
                pass
            else:
                #send to team view always, except for lat/long data
                pass
    except Exception as e:
        #on error, pass. log error in MQTT Error Log
        MQTTError.objects.create(module='mqtt', event='receive', message=f'{e}', error=True, time=datetime.now(), trip=Trip.objects.last())


def subscribe(topic, client: mqtt_client):
    def on_message(client, userdata, msg):
        store(msg)
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    for topic in topics:
        subscribe(topic, client)
    client.loop_forever()


def publish(client, topic, message):
    client.publish(topic, message)

# def send_location(lat, long):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)("teamdata", {"type": f"team.notif", "module": f"daq.location", "content": {"lat": lat, "long": long}, "error": False})

# def test_senddata(channel, module, content, type1):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(channel, {"type": type1, "module": module, "content": content, "error": False})
def test_mqttStress(numPerSec):
    client1 = connect_mqtt()
    ct = 0
    while ct < numPerSec:
        for key, val in topics.items():
            # print(key)
            client1.publish(key, randint(-5,100))
            time.sleep(1/numPerSec)
            ct +=1
