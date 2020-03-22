# dhl
DHL API测试工具

## 验证信息
### 测试环境
在脚本运行目录创建文件credentials，内容格式如下：  
```
username:password
2222222222_customer:uBQbZ62!ZiBiVVbhc
```

把第一行中username和password分别替换成DHL Entwickler Portal登录用户名和密码。第二行为测试帐号，无需进行修改。  

### 生产环境
```
AppId:token
user:pwd
```
第一行中AppId为用于处理API请求的Application ID，token为使用该Application的口令，这两项信息可在DHL开发者后台的Release&Operation获取。
第二行中的user必须在DHL商业用户后台生成，生成并激活后即可使用该用户调用API。user即为用户名，pwd为密码。

## HTTP数据格式
运行目录中的data.json为生成DHL Retoure面单所需数据，格式为json，作为HTTP数据提交。reveiverId为收件人代号，测试环境中通常是国家代码，如DE等。生成环境中的receiverId可以在商业用户后台中获取，对于一个商业用户来讲该id是唯一的。

完成上述准备工作后运行脚本：
```
python returns.py
```
如果运行成功会在当前目录生成文件名为Retoure.pdf的文件，即所需的DHL Retoure面单。
