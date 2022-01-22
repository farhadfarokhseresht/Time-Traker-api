from rest_framework import serializers
from .models import *
import datetime


class TimeTracker_serializers(serializers.ModelSerializer):
    class Meta:
        model = TimeTracker
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['start_at'] > validated_data['end_at']:
            raise serializers.ValidationError("The start time must be later than the end time !")
        else:
            obj = super().create(validated_data)
            obj.save()
            return obj

    def update(self, instance, validated_data):

        if validated_data['start_at'] > validated_data['end_at']:
            raise serializers.ValidationError("The start time must be later than the end time !")
        else:
            obj = super().update(instance, validated_data)
            obj.save()
            return obj
