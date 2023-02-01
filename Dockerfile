FROM python:3.8.0-stretch
# 配置工作目录
WORKDIR /ximalaya_live

# 拷贝当前目录所有的文件，进入 docker 镜像中
COPY . .

ADD . /ximalaya_live

RUN pip install -r requirements.txt

CMD python app.py