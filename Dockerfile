#FROM python:3.8.0-stretch
#拉取原始镜像
FROM harbor102.test.ximalaya.com/common/growth-custom-python3-base:v0.0.1
#打上个人标签
MAINTAINER dx_content<rou.zhang@ximalaya.com>
mkdir release
RUN mkdir -p /release
# 拷贝当前目录所有的文件，进入 docker 镜像中
COPY ./ximalaya_live/* ./release
#添加权限
RUN chmod +x /release/run.sh && sh /release/run.sh
#在镜像内安装依赖包
RUN pip install --upgrade pip && pip3 install -r requirement
# 进入镜像工作目录
WORKDIR /release
CMD ["/bin/sh", "-c", "/release/run.sh"]
CMD python main.py

###COPY ximalaya_live /usr/local/tfs-publish/ximalaya_live
###更改权限至最高等级
##RUN chmod-R 777 /ximalaya_live
####复制run.sh文件至镜像当前工作目录
###RUN release/run.sh
###进入以下工作目录
##WORKDIR /ximalaya_live
###运行文件
##CMD python main.py
#FROM harbor102.test.ximalaya.com/common/growth-custom-python3-base:v0.0.1

#COPY ./ximalaya_live/* ./release
#
#RUN chmod +x /release/run.sh && sh /release/run.sh
#
#CMD ["/bin/sh" "-c" "/release/run.sh"]