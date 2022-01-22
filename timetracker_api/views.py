from rest_framework.decorators import api_view
from rest_framework.response import Response
from timetracker_api.models import *
from rest_framework import status
import datetime


def TimeTracker_set(request, TimeTracker_instance):
    if 'start_at' in request.data:
        TimeTracker_instance.start_at = request.data['start_at']  # check data entry !!!
    if 'description' in request.data:
        TimeTracker_instance.description = request.data['description']  # check data entry !!!
    # if 'project' in request.data:
    #     TimeTracker_instance.project = request.data['project']
    # if 'tags' in request.data:
    #     TimeTracker_instance.tags = request.data['tags']
    if 'billable' in request.data:
        TimeTracker_instance.billable = request.data['billable']  # check data entry !!!
    if 'end_at' in request.data:
        TimeTracker_instance.end_at = request.data['end_at']  # check data entry !!!
    return TimeTracker_instance


@api_view(['POST', 'GET', 'PATCH', 'PUT', 'DELETE'])
def time_tracker(request):
    # Add a new time entry
    if request.method == 'POST':
        start_at = datetime.datetime.now()
        TimeTracker_instance = TimeTracker(start_at=start_at)
        TimeTracker_instance = TimeTracker_set(request, TimeTracker_instance)
        TimeTracker_instance.save()
        return Response({"message": "Add new time entry done successfully"}, status=status.HTTP_200_OK)

    # Stop currently running timer
    if request.method == 'PATCH':
        if 'TimeTracker_id' in request.data:
            TimeTracker_instance = TimeTracker.objects.get(id=request.data['TimeTracker_id'])  # check data entry !!!
            TimeTracker_instance.end_at = datetime.datetime.now()
            if 'end_at' in request.data:
                TimeTracker_instance.end_at = request.data['end_at']  # check data entry !!!
            TimeTracker_instance.save()
            return Response({"message": "Stop currently running timer done successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Currently running time entry was not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update time entry
    if request.method == 'PUT':
        if 'TimeTracker_id' in request.data:
            TimeTracker_instance = TimeTracker.objects.get(id=request.data['TimeTracker_id'])  # check data entry !!!
            TimeTracker_instance = TimeTracker_set(request, TimeTracker_instance)
            TimeTracker_instance.save()
            return Response({"message": "Update time entry done successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Currently time entry was not found"}, status=status.HTTP_404_NOT_FOUND)

    # Delete time entry
    if request.method == 'DELETE ':
        if 'TimeTracker_id' in request.data:
            TimeTracker_instance = TimeTracker.objects.get(id=request.data['TimeTracker_id'])  # check data entry !!!
            TimeTracker_instance.delete()
            return Response({"message": "Delete time entry done successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Time entry with given ID doesn't exist or doesn't belong"}, status=status.HTTP_404_NOT_FOUND)
