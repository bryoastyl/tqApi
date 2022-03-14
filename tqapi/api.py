import requests

url = "https://fidelity-shield-insurance-company-ltd.docuware.cloud/DocuWare/Platform/FileCabinets/3f46a7a1-d2aa-430f-a89a-fc5907f4bdc3/Documents?count=5000"

payload = {}
headers = {
    'Accept': 'application/xml',
    'Accept': 'application/json',
    'User-Agent': 'curl/7.68.0',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
