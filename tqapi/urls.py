from django.urls import path
from tqapi import services
from .views import TqApiViewSet
from tqapi import views

urlpatterns = [
    path('', views.get_docs, name="get_docs"),
    # path('tq/<int:id>/', views.tq_detail, name="tq_detail"),
    path('api',
         TqApiViewSet.as_view({'get': 'list'}), name='api'),
    path('api/input/<int:id>', TqApiViewSet.as_view(
        {'get': 'retrieve'}), name='api-retrieve'),
]
