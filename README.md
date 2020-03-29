# Mpy-Web-Alert
## 1，什么是Mpy-Web-Alert ？What this?
*一个简单的网页访问+提醒小功能，基于ESP8266+MicroPython+Websocket*  
### 功能介绍
监控页面是否有人访问：如果有人访问ESP8266 板载LED（Pin2）会进行1S的闪亮  
目前已经记录访问者的IP以及访问位置，修改后可以在屏幕显示
### 目录结构
- host  
......ipmsg.json 用来在服务器记录具体访问情况  
......ws.py 服务器启动服务的入口文件  
- mpy
......client.py websocket核心文件  
......protocol.py  
......logging.py  
......main.py  micro python启动默认执行文件
- web  
......web.html
## 2，如何使用 ？How to use?
- 修改host目录下main.py文件内监听服务的端口，默认为2233端口
- 运行 ```python ws.py```
- 修改web目录下web.html文件内对应的ws 服务地址，并上传至服务器
- 在需要的监控是否有人访问的页面使用iframe引入  
```<iframe src='web.html' style='display:none;'>```
- 修改mpy目录下main.py文件内具体链接端口与WIFI链接信息
- 上传mpy目录下所有文件至ESP8266
- 重启ESP8266
- 访问你要监控的页面，你的ESP8266是不是会亮一下呢
## 3，注意
写这个功能纯属个人爱好，代码目前存在着很大的优化空间，可能还存在着不可预知的BUG，但我会逐渐的完善和修复。如果您感兴趣，请点亮star👍，谢谢。最后您也可以移步本人博客：[歪克士www.wicos.me](https://www.wicos.me)查看更多内容。
