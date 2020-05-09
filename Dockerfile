FROM python:3

WORKDIR /usr/src/app

ADD ./ .

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
    && pip install --no-cache-dir -U "https://code.aliyun.com/wang0618/pywebio/repository/archive.zip?ref=dev" \
    && python3 -c "import bokeh; bokeh.sampledata.download()"

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

EXPOSE 8080

CMD python run.py