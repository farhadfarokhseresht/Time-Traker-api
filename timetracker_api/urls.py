from django.urls import path
from timetracker_api import views

urlpatterns = [
    path("time_tracker", views.time_tracker),
    path("time_tracker/<int:pk>", views.time_tracker_pk)
]