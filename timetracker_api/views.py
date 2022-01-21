from rest_framework.decorators import api_view
from rest_framework.response import Response
from timetracker_api.models import *
import datetime


@api_view(['POST', 'GET'])
def start_time_tracker(request):
    start_at = datetime.datetime.now()
    TimeTracker_instance = TimeTracker(start_at=start_at)
    # if request.method == 'POST':
    if 'description' in request.data:
        TimeTracker_instance.description = request.data['description']
    if 'project' in request.data:
        TimeTracker_instance.project = request.data['project']
    if 'tags' in request.data:
        TimeTracker_instance.tags = request.data['tags']
    if 'billable' in request.data:
        TimeTracker_instance.billable = request.data['billable']

    print(TimeTracker_instance.billable)

    return Response({"message": start_at})
