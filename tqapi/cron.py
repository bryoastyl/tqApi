from urllib import response
import requests
import os
import json
from tqApi import settings

from .models import Docuware


def get_docs():
    """
    Runs every min, updating and adding new documents
    """
    url = "https://fidelity-shield-insurance-company-ltd.docuware.cloud/DocuWare/Platform/FileCabinets/3f46a7a1-d2aa-430f-a89a-fc5907f4bdc3/Documents?count=10s00"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'PostmanRuntime/7.26.8',
        'Connection': 'keep-alive',
        'Cookie': settings.COOKIE,
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    datas = json.loads(response.text)
    req = datas['Items']

    for item in req:
        for field in item["Fields"]:
            if field["FieldLabel"] == "Document ID":
                Document_ID = (field.get("Item", "-"))
            if field["FieldLabel"] == "Amount ":
                Amount = (field.get("Item", "-"))
            if field["FieldLabel"] == "Payee Name":
                Payee_Name = (field.get("Item", "-"))
            if field["FieldLabel"] == "Payment Requisition Number":
                Payment_Requisition_Number = (field.get("Item", "-"))
            if field["FieldLabel"] == "FMS Process":
                FMS_Process = (field.get("Item", "-"))
            if field["FieldLabel"] == "TQ Status":
                TQ_Status = (field.get("Item", "|"))

        doc = Docuware(Document_ID=Document_ID, Amount=Amount, Payee_Name=Payee_Name,
                       Payment_Requisition_Number=Payment_Requisition_Number, FMS_Process=FMS_Process, TQ_Status=TQ_Status)
        doc.save()


get_docs()
