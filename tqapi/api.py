import requests

url = "https://fidelity-shield-insurance-company-ltd.docuware.cloud/DocuWare/Platform/FileCabinets/3f46a7a1-d2aa-430f-a89a-fc5907f4bdc3/Documents?count=5000"

payload={}
headers = {
  'Accept': 'application/xml',
  'Accept': 'application/json',
  'User-Agent': 'curl/7.68.0',
  'Cookie': 'ApplicationGatewayAffinityCORS=60510e90b06cfa88f0d0faae08b72b6f; ApplicationGatewayAffinity=60510e90b06cfa88f0d0faae08b72b6f; .DWPLATFORMAUTH=065ED22B15C9757EAB03D400ABF50D0DE1E71CCABE40B71A30FF7B34DB391A0B8873A5B6DABE42B0703B6D18258A31BC58BDFE94DDD7AB49315541215FCA42F89335B95463E542654378FF3D86B9CE9A91B391C9AD7DAD6A794A8AA71901D27BBBAB8FF2B5B3EE2AA3B6888BEFCFED51D46298D1E8158709BD236BA68108C47C5DA98F3B9B69127F3BDFBF9C48B14554F0D0D47DDE7FA4CE248D41518B2253C5F29734D9E4CD9B8BBBFE9F9A28A5D4A4778BA70E33E6E4DF3BCEB85A99CA150E1780DB9E57346E8D34C6013169741DF18B5C157805212E4530B122D6013E30C603D0D26CF594F0A90A546E1DC1DDD77139CA4F218966E96C6BC65FF08CCB375EAE26BFAA5C366BAD9E45A221F4519BD121C97B7BEB8D3FCEF932720217BE82072608B663A1415EA0EE9DC205F7806B64D10BBDE026A08949F27D345703E67B65E0BB4F28D6965D909C671DE9686282A37DF580E5889044FF5E1E052EE32DBDF32C3D0EAE2AE7FDD92B620A03F6EF54299CF7A5FB6661AD495E80FF1C460FEE7FAAB10D78F1D3F7CC43C7BDDC25AB672DC38861B622802E37AF42896258A6168712B4203403AC5125356ADD654E7A0EDF2C3F52DE56E4D0B02B1029CFFFC76DFD; DWPLATFORMBROWSERID=E345A46E553A71EAC7701A903E871FF631D7C1FCC14CBAA6A7E79690FF65B6093A217CB1D18E501D1D1AD1A359F4EE47D4E427BE1A1C470F8AD6571D2DCC1D51C91D9E1ECEE902402227931A5FB7B8C7C4735EA535DD770B84B9359C68FCBF07F5CF677A4B91FA2AB1EFD23848F45AD6F13D0FAF6675E9F2395738BBBEC930A4F079A5FAF78AD72CDE6DCA0EF3FFF1A93459C1CD706F0C3340DF74D2F07424381F0BBA9277B6791E5E6D0164AD9B596DE1CFEA94794864D30C106DFF2A12F41B18A483BF81A0648DF45BDD9A6DF8B24625F158E1279F60F5808D6F4B5DD79F7A3A28ED121D7A7A2CD7E28BBB514CEF9CE8E975288DB9A1089438067F868F9614'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
