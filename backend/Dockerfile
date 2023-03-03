#FROM python:3.8.0-stretch
#拉取原始镜像
FROM centos
#FROM harbor102.test.ximalaya.com/test
#打上个人标签
MAINTAINER dx_content<rou.zhang@ximalaya.com>
#创建工作目录
RUN mkdir -p /release
# 拷贝当前目录所有的文件，进入 docker 镜像中
ADD  ./ximalaya_live  /release
#添加权限
RUN #chmod u+x /release && sh /release
RUN chmod u+x /release
#在镜像内安装依赖包
RUN pip install --upgrade pip && pip3 install -r requirement
# 进入镜像工作目录
WORKDIR /release/backend
ENV FLASK_APP=app.py
EXPOSE 80
CMD ["python","main.py"]
