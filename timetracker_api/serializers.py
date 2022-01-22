from rest_framework import serializers


class TimeTracker_serializers(serializers.Serializer):
    description = serializers.CharField()
    billable = serializers.BooleanField(required=True)
    start_at = serializers.DateTimeField(required=True)
    end_at = serializers.DateTimeField()
