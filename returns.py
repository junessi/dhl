import requests
import base64
import json
import sys

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
      'Authorization': "Basic " + base64.b64encode(authentication.encode('utf-8')).decode('utf-8'),
      'DPDHL-User-Authentication-Token': base64.b64encode(authorization.encode('utf-8')).decode('utf-8')
    }
    print(headers)

    resp = requests.post(url, headers = headers, json = payload)

    if resp.status_code > 201:
        err_msg = "status code {0}: {1}".format(resp.status_code, resp.content)
        print(err_msg)
        sys.exit()
    else:
        print("successful")

    # returnDocumentType in data.json could one of ["SHIPMENT_LABLE", "QR_LABLE", "BOTH"]
    data = resp.json()
    if "labelData" in data and data["labelData"] is not None:
        labelData = data["labelData"]
        filename = "Retoure.pdf"
        f = open(filename, "wb")
        f.write(base64.b64decode(labelData))
        f.close()
        print("Saved to {0}".format(filename))
    elif "qrLabelData" in data and data["qrLabelData"] is not None:
        qrLabelData = data["qrLabelData"]
        filename = "qrcode.png"
        f = open(filename, "wb")
        f.write(base64.b64decode(qrLabelData))
        f.close()
        print("Saved to {0}".format(filename))
    else:
        print(data)
else:
    print("failed to prepare credential data")

