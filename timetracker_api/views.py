from rest_framework.decorators import api_view
from rest_framework.response import Response
from timetracker_api.models import *
from rest_framework import status
import datetime


@api_view(['POST', 'GET', 'PATCH', 'PUT', 'DELETE'])
def time_tracker(request):
    # Add a new time entry
    if request.method == 'POST':
        start_at = datetime.datetime.now()
        TimeTracker_instance: TimeTracker = TimeTracker(start_at=start_at)
        if 'description' in request.data:
            TimeTracker_instance.description = request.data['description']
        # if 'project' in request.data:
        #     TimeTracker_instance.project = request.data['project']
        # if 'tags' in request.data:
        #     TimeTracker_instance.tags = request.data['tags']
        if 'billable' in request.data:
            TimeTracker_instance.billable = request.data['billable']
        TimeTracker_instance.save()
        return Response({"message": "OK0"}, status=status.HTTP_200_OK)

    # Stop currently running timer
    if request.method == 'PATCH':
        if 'TimeTracker_instance_id' in request.data:
            TimeTracker_instance = TimeTracker.objects.get(id=request.data['TimeTracker_instance_id'])
            print(TimeTracker_instance.description)
            return Response({"message": "OK1"}, status=status.HTTP_200_OK)
        else:
            TimeTracker_instance = TimeTracker.objects.latest('id')
            print(TimeTracker_instance.description)
        return Response({"message": "OK2"}, status=status.HTTP_200_OK)
