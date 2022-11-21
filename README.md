## 使用说明
编写config.xml文件：配置发件人信息、收件人信息、每天发邮件的时间，需要自行申请qq邮箱的pop3码。配制好后直接运行<br />
`python run.py`
## docker部署
打包镜像：`docker build -t xxx .`<br />
启动项目：`docker run --name xxx -itd image_id`

## 支持打包为可执行文件

第一步：`pip install pyinstaller`

第二步：根目录打包文件`pyinstaller -D ./run.py`

第三步：把除了run.py以外的文件都放到dist/run目录下

第四步：点击生成的可执行文件（Windows 双击.exe文件，MacOS执行./run.sh，如果不成给文件加可执行权限`sudo chmod 777 run.sh`再运行就可）

## 配置环境(所有包都没有强制的版本要求，若下载不成功就下载能用的版本就好)
`pip install -r requirements.txt`
## linux后台挂起运行
`nohup python run.py 2>nohup.log &`
## 百度天气api
https://lbsyun.baidu.com/apiconsole/key
## 天行数据api
https://www.tianapi.com/apiview/174

## 效果图<br/>

![效果图](https://github.com/Ska-cloud/auto_send_daily_temperature_email/blob/main/IMG_0707.GIF)
