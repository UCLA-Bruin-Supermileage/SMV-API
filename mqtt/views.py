from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from .helper import run, test_mqttStress
from .models import Trip
import threading
import json
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import Group, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets
from .serializers import TripSerializer, UserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, action

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
- Can GET /api/trip/: return all trips. NO AUTHENTIATION REQUIRED
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
    serializer_class = TripSerializer
    def get_permissions(self):
            #allow no authentication for get
            if self.action in ['list', 'retrieve', 'last']:  
                return [permissions.AllowAny()]  # No authentication needed for GET
            return [permissions.IsAuthenticated()]  
    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def last(self, request, *args, **kwargs):
        """
        return trip with highest ID
        """
        trip = Trip.objects.all().order_by('-id').first()
        if trip:
            serializer = self.get_serializer(trip)
            return Response(serializer.data)
        return Response({'detail': 'No trips found'}, status=404)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Fetch trips
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
    
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", daemon=True)
thread.start()
