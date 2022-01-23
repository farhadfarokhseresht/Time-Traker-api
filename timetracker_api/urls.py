from django.urls import path
from timetracker_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('time_tracker', views.time_trackerViewSet)

urlpatterns = [
    # path("time_tracker", views.time_tracker),
    # path("time_tracker/<int:pk>", views.time_tracker_pk)
]

urlpatterns += router.urls