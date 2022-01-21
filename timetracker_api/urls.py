from django.urls import path
from timetracker_api import views

urlpatterns = [
    path("start_time_tracker", views.start_time_tracker),
    path("stop_time_tracker", views.stop_time_tracker),
]