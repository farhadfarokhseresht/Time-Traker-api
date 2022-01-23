from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status
import datetime
from .serializers import TimeTracker_serializers
from rest_framework import viewsets


class  TimeTrackerViewSet(viewsets.ModelViewSet):
    queryset = TimeTracker.objects.all()
    serializer_class = TimeTracker_serializers
    http_method_names = ['get', 'post', 'put', 'delete']