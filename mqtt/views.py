from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from .helper import run, test_mqttStress
from .models import Trip, SpeedData, RPMData, Accel, Magnetometer, Gyro_x, Gyro_y, Gyro_z
from .topics import topics_list as topics
import threading
import json
from datetime import datetime, date
import csv
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .serializers import TripSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

def index(request):
    return render(request, 'mqtt/dashboard.html')

def map(request):
    #temp map view 
    return render(request, 'mqtt/map.html')

def dash_admin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if not request.user.is_authenticated:
            return Http404()
        match data['feature']:
            case "increment_trip":
                if data['data'] is not None:
                    Trip.objects.last().active = False
                    Trip.objects.create(name=data['data'], date_created=datetime.now(), active=True)
            case "test_mqtt":
                test_mqttStress(6600)
                print("done")
        return JsonResponse({"status": "200"})
    else:
        recent_trip = Trip.objects.last()
        return render(request, 'mqtt/dashboard_admin.html', {
            "trip": recent_trip,
        })
    
def team_view(request):
    return render(request, 'mqtt/team_dash.html')

"""
API Endpoint: /api/trip/<int:id (optional)>
API endpoint that allows trips to be viewed or edited.
- Can GET /api/trip/: return all trips. NO AUTHENTICATION REQUIRED
- Can POST /api/trip/: 
    {
        "name": "",
        "date_created": YYYY-MM-DD,
        "start": YYYY-MM-DD:HH:mm,
        "stop": null
    }
    REQUIRES AUTHENTICATION
"""
class TripViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication] # 
    # permission_classes = [permissions.IsAuthenticated] # 
    queryset = Trip.objects.all()
    serializer_class = TripSerializer #includes default actions
    def get_permissions(self):
            #allow no authentication for get
            if self.action in ['list', 'retrieve', 'last', 'post']:  
                return [permissions.AllowAny()]  # No authentication needed for GET
            return [permissions.AllowAny()]  
    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def last(self, request, *args, **kwargs):
        """
        return trip with highest ID, or last trip
        """
        trip = Trip.objects.all().order_by('-id').first()
        if trip:
            serializer = self.get_serializer(trip)
            return Response(serializer.data)
        return Response({'detail': 'No trips found'}, status=404)
    @extend_schema(
            parameters = [OpenApiParameter(name='name', description="New Trip Name", type=OpenApiTypes.STR, required=True)],
    )
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def start(self, request, *args, **kwargs):
        """
        Create a new trip with start time now, name from request \n
        Input: {"name": "trip_name"} \n
        Returns: New Trip JSON
        """
        trip = Trip.objects.create(name=request.data['name'], date_created=date.today(), start=datetime.now())
        trip.save()
        serializer = self.get_serializer(trip)
        return Response(serializer.data)
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def export(self, request, *args, **kwargs):
        sensor = request.data.get('sensor')
        requestID = request.data.get('trip_id')
        formatRequested = request.data.get('format')

        if not requestID:
            return Response({"error": "Missing request ID"}, status=400)
        
        requestId = int(requestID)

        # topics[msg.topic]['model'].objects.create(date=datetime.now(), data=payload, trip=Trip.objects.last()) 
        
        model = topics[sensor]['model'].objects.filter(id=requestID).first()

        if(formatRequested == 'json'):
            serializer = self.get_serializer(model)
            return Response(serializer.data)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sensor_data.csv"'
        writer = csv.writer(response)
        writer.writerow(['Date', 'Data', 'Trip'])
        writer.writerow([model.date, model.data, model.trip])
        return response

    def list(self, request, *args, **kwargs):
        """
        List all trips, no authentication required
        """
        queryset = self.get_queryset()  # Fetch trips
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class StartStop(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication] # 
    permission_classes = [permissions.IsAuthenticated] # 
    def create(self, request):
        data = request.data
        trip = Trip.objects.last()
        if trip:
            if data['start']:
                trip.start = datetime.now()
            if data['stop']:
                trip.stop = datetime.now()
            trip.save()
            return Response({'status': '200'})
        return Response({'detail': 'No trips found'}, status=404)
# def login_view(request):
#     if request.method == "POST":
#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("dash_admin"), status=302)
#         else:
#             return render(request, "mqtt/dashboard_admin.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         raise Http404

#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", daemon=True)
thread.start()
