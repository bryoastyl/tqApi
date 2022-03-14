from django.urls import path
from tqapi import cron
from .views import TqApiViewSet
from tqapi import views

urlpatterns = [
    path('api', TqApiViewSet.as_view(
        {'get': 'list'}), name='api'),
    path('api/input/<int:id>', TqApiViewSet.as_view(
        {'get': 'retrieve'}), name='api-retrieve'),
]
