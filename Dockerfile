#FROM python:3.8.0-stretch
#拉取原始镜像
FROM silverlogic/python3.6
#FROM harbor102.test.ximalaya.com/test/ximalaya_live:$1
#打上个人标签
MAINTAINER ximalive-qa<rou.zhang@ximalaya.com>
RUN apt-get update && apt-get install python3-pip python3-pymysql -y libsm6 libxext6 libxrender-dev; apt-get autoclean; rm -rf /var/lib/apt/lists/*
#创建工作目录
RUN mkdir -p /usr/local/tfs-publish/ximalaya_live
# 拷贝当前目录所有的文件，进入 docker 镜像中
COPY  ./  ./usr/local/tfs-publish/ximalaya_live
WORKDIR /usr/local/tfs-publish/ximalaya_live
#COPY pip.conf /etc/pip.conf
#添加权限
RUN chmod u+x /usr/local/tfs-publish/ximalaya_live
#RUN cp ximalaya_live/backend/run.sh .
#WORKDIR /usr/local/tfs-publish/ximalaya_live/frontend
##前端项目打包
# 进入镜像工作目录
WORKDIR /usr/local/tfs-publish/ximalaya_live/backend
#在镜像内安装依赖包
RUN pip install --upgrade pip && pip3 install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
#CMD ["sh","run.sh"]
ENV FLASK_APP=app.py
ENV TZ="Asia/Shanghai"
EXPOSE 7169
CMD ["sh","-c","nohup run.sh > tmp/log.out 2>&1 && sleep shinfinity"]
CMD ["python","main.py"]

