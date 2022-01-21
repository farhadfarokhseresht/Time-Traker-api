from django.urls import path
from timetracker_api import views

urlpatterns = [
    path("start_time_tracker", views.start_time_tracker),
]