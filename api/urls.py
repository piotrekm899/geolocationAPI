from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from rest_framework.routers import SimpleRouter

from .views import GeolocationViewSet

router = SimpleRouter()
router.register("geolocations", GeolocationViewSet, basename="geolocation")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
