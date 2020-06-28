import requests
import base64
import jinja2

f = open("credentials", "r")
authorization = f.readline().rstrip('\n') # read authorization data
authentication = f.readline().rstrip('\n') # read authentication data
f.close()

if authorization and authentication:
    print("credential data is ready")

    url="https://cig.dhl.de/services/production/soap"
    f = open("createShipmentOrder.xml", "r")
    body = f.read()
    f.close()

    t = jinja2.Template(body)
    [auth_username, auth_password] = authorization.split(':')
    body = t.render(username = auth_username, password = auth_password)

    headers = {
        'Content-Type': 'application/soap+xml;charset=utf-8',
        'Accept-Encoding': 'gzip,deflate',
        'SOAPAction': 'urn:createShipmentOrder',
        'Authorization': "Basic " + base64.b64encode(authentication.encode('utf-8')).decode('utf-8')
    }
    print(base64.b64encode(authentication.encode('utf-8')).decode('utf-8'))

    response = requests.post(url, data=body, headers=headers)
    print(response.content)
