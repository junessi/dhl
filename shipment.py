import requests
import base64

f = open("credentials", "r")
authorization = f.readline().rstrip('\n') # read authorization data
authentication = f.readline().rstrip('\n') # read authentication data
f.close()

if authorization and authentication:
    print("credential data is ready")

    url="https://cig.dhl.de/services/production/soap"
    f = open("createShipmentOrder.xml", "r")
    body = f.read()
    print(body)
    f.close()

    headers = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'Accept-Encoding': 'gzip,deflate',
        'SOAPAction': 'urn:createShipmentOrder',
        'Authorization': "Basic " + base64.b64encode(authentication.encode('utf-8')).decode('utf-8')
    }

    response = requests.post(url, data=body, headers=headers)
    print(response.content)
