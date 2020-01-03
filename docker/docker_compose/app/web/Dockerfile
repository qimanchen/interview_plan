# 定义一个镜像
# 安装python包
# 并启动该应用程序
FROM python:2.7
COPY ./ /web/
WORKDIR /web
RUN pip install -r requirements.txt
CMD python web.py