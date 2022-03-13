from urllib import response
import requests
import os
import json

from .models import Docuware


def get_docs():
    """
    Runs every min, updating and adding new documents
    """
    url = "https://fidelity-shield-insurance-company-ltd.docuware.cloud/DocuWare/Platform/FileCabinets/3f46a7a1-d2aa-430f-a89a-fc5907f4bdc3/Documents/"
    # url to have count
    payload = {}
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'PostmanRuntime/7.26.8',
        'Connection': 'keep-alive',
        'Cookie': '.DWPLATFORMAUTH=A7945D6E943424921F23A2F86BD009BB6749392F867995E5CA05FB75A5BDA1F10BBE27B1733BDC261DABEEC621751B18E173456145EBDF07E7F9524912D3A8781BF1603F54ADACADB751E265E932797DEB7E5F9886264D68DC91E2B815496A1E79F8454050144C937CFF4A64D93CE8F9777F060B522DB8C0DAD5441988BC4D54213692FB2A6DC024FA85D74F5CB7298318057596395334FFA09F747D78CFD6E52AAD8804D7A755E27BA81226DEBCAE9E23C396B9714ED1FB503E26773767F0C78D06E0DDCFC43635855113B99D8008783F1ABFAC71E8862C8B02384711BBE45A260191052E586F57D3D114D04549667E2E216BDC1E66AE07D9D8E81A7DCAACE4C17E20667064B1216C1A35E96A8A1C44C55E4610895753FACDE1CB9A4E2FC84387FA411608A6CFB1A1F745AE61960E6F85A8E6B0887C8371539A6D4CE9BF4C9C4CE8BB812ED53A6DC19E410627B7BC33164205211ED6E84A309610E3D0A9C0D9148FD26BCC9BA2C355ECF137800A28C33084E22A9FFCEE79B144C5EAF0E2D581BFAD3EBFDEC5149A0928CF0F633AB89C8657D547108EAA6F292D7A0EA4C6D5712171F769DEDA8A952C5F1DFF9267C4D015C76952E3AF835DB00BE23EF44EF311; ApplicationGatewayAffinity=999423437733d55a1cacbcac06429e68; ApplicationGatewayAffinityCORS=999423437733d55a1cacbcac06429e68; DWPLATFORMBROWSERID=FFDCE8CC14F9EBBA0E0F452C36BB597F0793A7BF482D2FC7E3506520592157BC39C4B36FD7FCB98DCEA21E0F1CD7184C38FC4029AA1F05B17908F65394353530C975CD14DC63CE04A1DFE76DB77E61B17BC90A753BDE2BAACA877628A79408EFAAC20CEFBC31BCF331F07EA1EEC69FF67F8A7782E1309EC20D03DF9BBD80CD4922D95AB6BE35733E77ABDE7DB34CDB7F7C245169B16578DE2C059C97F429A8D9EFBD3D304D741522534B19280931E943C6E19B006E8D625DF556270D7D9D722F8DE07FCFB545055D5DF34004DD86FDFCC859657A082D58AAF355224B69EB9D6AD88C7E50327DCD597D65B9B4F7EA7D2F9D2689E5E09624EC3F32AE8FAD4E4A86'
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    datas = json.loads(response.text)
    req = datas['Items']
    # print(req)
    for item in req:
        for field in item["Fields"]:
            if field["FieldLabel"] == "Document ID":
                Document_ID = (field.get("Item", "-"))
                print(Document_ID)
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
