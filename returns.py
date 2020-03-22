import requests
import base64
import json

f = open("credentials", "r")
authorization = f.readline().rstrip('\n') # read authorization data
authentication = f.readline().rstrip('\n') # read authentication data
f.close()

f = open("data.json", "r")
payload = json.load(f)
f.close()

if authorization and authentication:
    print("credential data is ready")

    # url = "https://cig.dhl.de/services/sandbox/rest/returns/"
    url = "https://cig.dhl.de/services/production/rest/returns/"
    headers = {
    'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': "Basic " + base64.b64encode(authorization.encode('utf-8')).decode('utf-8'),
      'DPDHL-User-Authentication-Token': base64.b64encode(authentication.encode('utf-8')).decode('utf-8')
    }
    print(headers)

    resp = requests.post(url, headers = headers, json = payload)
    data = resp.json()
    if "labelData" in data:
        labelData = data["labelData"]
        f = open("Retoure.pdf", "wb")
        f.write(base64.b64decode(labelData))
        f.close()
    else:
        print(data)
else:
    print("failed to prepare credential data")

