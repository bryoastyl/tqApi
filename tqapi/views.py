from django import views
from django.shortcuts import render
import os
from django.db.models import Q
from tqapi.models import Docuware
from tqapi import cron

from .serializers import TqApiSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import os
from django.shortcuts import render


from tqapi.models import Docuware


class TqApiViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TqApiSerializer

    def list(self, request):
        cron.get_docs()
        queryset = Docuware.objects.exclude((Q(Payment_Requisition_Number__gt=1) & Q(
            TQ_Status='PENDING')) | Q(TQ_Status__in=['COMPLETED', '|']))
        serializer = self.serializer_class(
            queryset, many=True, context={'request': request})
        return Response(dict(success=True, data=serializer.data, message="All items"))

    def retrieve(self, request, id=None):
        queryset = Docuware.objects.get(id=id)
        serializer = self.serializer_class(
            queryset, context={'request': request})
        return Response(dict(success=True, message='The Document was retrieved successfully', data=serializer.data))
