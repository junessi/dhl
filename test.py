import base64
import requests
import json

url = "https://cig.dhl.de/services/sandbox/rest/returns/"
f = open("credentials", "r")
authorization = f.readline().rstrip('\n') # read authorization data
authentication = f.readline().rstrip('\n') # read authentication data
f.close()

# f = open("data.json", "r")
# payload = json.load(f)
# payload = "{\"receiverId\": \"DE\",\"customerReference\": \"123456789\",\"shipmentReference\": \"Sendungsreferenz\",\"senderAddress\": {\"name1\": \"Empf?nger Retoure Zeile 1\",\"name2\": \"Empf?nger Retoure Zeile 2\",\"name3\": \"Empf?nger Retoure Zeile 3\",\"streetName\": \"Vegesacker Heerstr.\",\"houseNumber\": \"111\",\"postCode\": \"28757\",\"city\": \"Bremen\",\"country\": {\"countryISOCode\": \"DEU\",\"country\": \"Germany\" }},\"email\": \"Max.Mustermann@test.de\",\"telephoneNumber\": \"+49 421 987654321\",\"weightInGrams\": 5000,\"returnDocumentType\": \"SHIPMENT_LABEL\"}"
payload = '{"receiverId": "DE","customerReference": "123456789","shipmentReference": "Sendungsreferenz","senderAddress": {"name1": "Empf?nger Retoure Zeile 1","name2": "Empf?nger Retoure Zeile 2","name3": "Empf?nger Retoure Zeile 3","streetName": "Vegesacker Heerstr.","houseNumber": "111","postCode": "28757","city": "Bremen","country": {"countryISOCode": "DEU","country": "Germany" }},"email": "Max.Mustermann@test.de","telephoneNumber": "+49 421 987654321","weightInGrams": 5000,"returnDocumentType": "SHIPMENT_LABEL"}'
print(payload)
headers = {
'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': "Basic " + base64.b64encode(authorization.encode('utf-8')).decode('utf-8'),
  'DPDHL-User-Authentication-Token': base64.b64encode(authentication.encode('utf-8')).decode('utf-8')
}

response = requests.post(url, headers=headers, data = payload)

print(response.text.encode('utf8'))
