from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status
import datetime
from .serializers import TimeTracker_serializers


def data_set(request):
    data = {}
    if 'start_at' in request.data:
        data['start_at'] = request.data['start_at']
    if 'description' in request.data:
        data['description'] = request.data['description']
    if 'billable' in request.data:
        data['billable'] = request.data['billable']
    if 'end_at' in request.data:
        data['end_at'] = request.data['end_at']

    serial = TimeTracker_serializers(data=data)
    return serial


@api_view(['POST', 'GET'])
def time_tracker(request):
    # Add a new time entry
    if request.method == 'POST':
        serial = data_set(request)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get all time entry
    if request.method == 'GET':
        obj = TimeTracker.objects.all()
        ser = TimeTracker_serializers(obj, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def time_tracker_pk(request, pk):
    try:
        timeTracker_obj = TimeTracker.objects.get(pk=pk)
    except:
        return Response({"error": "Currently  time entry was not found !"}, status=status.HTTP_404_NOT_FOUND)

    # Get a specific time entry
    if request.method == 'GET':
        ser = TimeTracker_serializers(timeTracker_obj)
        return Response(ser.data, status=status.HTTP_200_OK)

    # Stop currently running timer
    elif request.method == 'PATCH':
        timeTracker_obj.end_at = datetime.datetime.now()
        timeTracker_obj.save()
        return Response("ok",status=status.HTTP_200_OK)

    # Update time entry
    elif request.method == 'PUT':
        ser = TimeTracker_serializers(timeTracker_obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete time entry
    elif request.method == 'DELETE':
        timeTracker_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
