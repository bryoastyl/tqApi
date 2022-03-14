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
    url = "https://fidelity-shield-insurance-company-ltd.docuware.cloud/DocuWare/Platform/FileCabinets/3f46a7a1-d2aa-430f-a89a-fc5907f4bdc3/Documents?count=500"
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
    # print(req)
    for item in req:
        for field in item["Fields"]:
            if field["FieldLabel"] == "Document ID":
                Document_ID = (field.get("Item", "-"))
                # print(Document_ID)
            if field["FieldLabel"] == "Amount ":
                Amount = (field.get("Item", "-"))
                # print(Amount)
            if field["FieldLabel"] == "Payee Name":
                Payee_Name = (field.get("Item", "-"))
                # print(Payee_Name)
            if field["FieldLabel"] == "Payment Requisition Number":
                Payment_Requisition_Number = (field.get("Item", "-"))
                # print(Payment_Requisition_Number)  # null, != null
            if field["FieldLabel"] == "FMS Process":
                FMS_Process = (field.get("Item", "-"))
                # print(FMS_Process)  # Cheque, Petty Cash, Eft
            if field["FieldLabel"] == "TQ Status":
                TQ_Status = (field.get("Item", "|"))

                # print(TQ_Status)  # Rejected, pending
            # else:
            #     print('All Documents are up to Date')

        doc = Docuware(Document_ID=Document_ID, Amount=Amount, Payee_Name=Payee_Name,
                       Payment_Requisition_Number=Payment_Requisition_Number, FMS_Process=FMS_Process, TQ_Status=TQ_Status)
        doc.save()


get_docs()
# doc_data.save()
# all_docs = Docuware.objects.all().order_by('-id')
# print(r.json())
# a = json.loads(data)
# docs = data['docs']
# # print(a)

# for i in r:

# return render(request, 'tq/tq.html', {"all_docs": all_docs})
# flat_list = [item in req for item in req]

# flat_list = []
# for sublist in req:
#     for item in sublist:
#         flat_list.append(item)
# print(flat_list)
# stat = json.dumps(req)
# print(stat)
# for i in req:
#     if i['FieldName'] == 'DWDOCID':
#         document_ID = i['Item']
#         print(document_ID)
# for i in req[0]['Fields']:
#     print(i)
# print(req)
# stat = req['FileCabinetID']
# print(stat)

# doc_data = Docuware(
#     print(item["Fields"][0]["Item"])  # Document ID

# )
# doc_data = Docuware(
# Document_ID = (item["Fields"][0]["Item"])
# Payee_Name = (item["Fields"][13].get("Item", "-"))  # Amount
# Amount = (item["Fields"][17].get("Item", "-"))  # Payee Name
# Payment_Requisition_Number = (item["Fields"][64].get(
#     "Item", "-"))  # Payment Requisition Number
# FMS_Process = (item["Fields"][65].get("Item", "-"))  # FMS Process
# TQ_Status = (item["Fields"][66].get("Item", "-"))  # TQ_STATUS
#         )
#         doc_data.save()
