from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'trip', views.TripViewset)
router.register(r'lastNData', views.LastNDataViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", views.dash_admin, name="dash_admin"),
    path("team-view", views.team_view, name="team_view"),
    # path("login", views.login_view, name="login"),
    path("speedometer", views.index, name="index"),

    #conceptual ideation for team dash
    path("test/map", views.map, name="map"),
]
