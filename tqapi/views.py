from django import views
from django.shortcuts import render
import os

from tqapi.models import Docuware

from .serializers import TqApiSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

import os
from django.shortcuts import render
import requests

from tqapi.models import Docuware


def get_docs(request):
    all_docs = {}
    if 'documentID' in request.GET:
        documentId = request.GET['documentId']
        url = 'https://fidelity-shield-insurance-company-ltd.docuware.cloud/DocuWare/Platform/FileCabinets/3f46a7a1-d2aa-430f-a89a-fc5907f4bdc3/Documents/' % documentId
        r = requests.get(
            url, headers={'Authorization': 'Bearer %s' % os.getenv('ACCESS_TOKEN')})
        print(os.getenv('ACCESS_TOKEN'))
        data = r.json()
        docs = data['docs']
        print(data)

        for i in docs:
            doc_data = Docuware(
                Document_ID=i['Document ID'],
                Payee_Name=i['Payee Name'],
                Amount=i['Amount '],
                Payment_Requisition_Number=i['Payment Requisition Number'],
                FMS_Process=i['FMS Process'],
                TQ_Status=i['TQ Status'],
            )
            doc_data.save()
            all_docs = Docuware.objects.all().order_by('-id')

    return render(request, 'tq/tq.html', {"all_docs": all_docs})


class TqApiViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving.
    """

    serializer_class = TqApiSerializer

    def list(self, request):
        queryset = Docuware.objects.all()
        serializer = self.serializer_class(
            queryset, many=True, context={'request': request})
        return Response(dict(success=True, data=serializer.data, message="All items"))

    def retrieve(self, request, id=None):
        queryset = Docuware.objects.get(id=id)
        serializer = self.serializer_class(
            queryset, context={'request': request})
        return Response(dict(success=True, message='The Document was retrieved successfully', data=serializer.data))
