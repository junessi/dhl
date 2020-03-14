# dhl
DHL API测试工具

## 验证信息
在脚本运行目录创建文件credentials，内容格式如下：  
```
username:password
2222222222_customer:uBQbZ62!ZiBiVVbhc
```

把第一行中username和password分别替换成DHL Entwickler Portal登录用户名和密码。第二行为测试帐号，无需进行修改。  

运行目录中的data.json为生成DHL Retoure面单所需信息模板，可根据需要进行修改。

完成上述准备工作后运行脚本：
```
python returns.py
```
如果运行成功会在当前目录生成文件名为Retoure.pdf的文件，即所需的DHL Retoure面单。
