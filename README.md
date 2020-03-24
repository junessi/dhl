# dhl
DHL API测试工具

## 验证信息
在脚本运行目录创建文件credentials，根据环境对credentials内容进行配置。
### 测试环境(sanbox)
```
username:password
2222222222_customer:uBQbZ62!ZiBiVVbhc
```

第一行中username和password分别为DHL Entwickler Portal登录用户名和密码。第二行为DHL官方提供的测试帐号，无需进行修改。  

### 生产环境(production)
```
AppId:token
user:pwd
```
第一行分别为Application的id和token，可以在DHL开发者后台Release&Operation中相应Application获取。
第二行分别为DHL商业后台生成的用户的用户名和密码。

## HTTP数据格式
运行目录中的data.json为生成DHL Retoure面单所需数据，格式为json，作为HTTP数据提交。数据示例：
```
{
  "receiverId": "deu",
  "customerReference": "123456789",
  "shipmentReference": "Sendungsreferenz",
  "senderAddress": {
    "name1": "Zhang San",
    "name2": "Li Si",
    "name3": "Wang Wu",
    "streetName": "Vegesacker Heerstr.",
    "houseNumber": "111",
    "postCode": "28757",
    "city": "Bremen",
    "country": {
      "countryISOCode": "DEU",
      "country": "Germany"
    }
  },
  "email": "Test.Mustermann@doval.de",
  "telephoneNumber": "+49 351 987654321",
  "weightInGrams": 5000,
  "returnDocumentType": "SHIPMENT_LABEL"
}
```
### reveiverId
收件人Id，测试环境中通常是国家代码，如DE等。生产环境中的receiverId商业用户预先设置好的收件人Id，每个收件人Id对应的收货地址将被自动填写在API返回的包裹单中。ReceiverId可以在商业用户后台中获取，一个商业用户可以拥有多个receiverId。
### customerReference
预留字段
### shipmentReference
预留字段
### senderAddress
发件人信息
### weightInGrams
包裹重量，单位为克。

完成上述准备工作后运行脚本：
```
python returns.py
```
返回结果示例如下：
```
{
  "shipmentNumber":"999990184381",
  "labelData":"JVBERi0xLjQKJeLjz9......",
  "qrLabelData":null,
  "routingCode":"40327653113+99000933090010"
}
```
### shipmentNumber
包裹单号
### labelData
被base64编码过的包裹pdf文件，对此字段进行base64解码即可得到包裹单pdf文件的原始数据。

如果运行成功会在当前目录生成文件名为Retoure.pdf的文件，即所需的DHL Retoure面单，可参见示例文件Retoure.pdf。
