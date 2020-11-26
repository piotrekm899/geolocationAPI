from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Geolocation
from .serializers import GeolocationSerializer, IPURLSerializer
from .external_api import call_ipstack


class GeolocationViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet,
                         ):

    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # check if the provided argument is valid before sending request(simple validation)
        ip_serializer = IPURLSerializer(data=request.data)
        ip_serializer.is_valid(raise_exception=True)

        # if argument is valid - send request to external api and fetch data
        request_data = call_ipstack(request.data["ip_or_url"])
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

