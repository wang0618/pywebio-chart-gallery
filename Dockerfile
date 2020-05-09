FROM python:3

WORKDIR /usr/src/app

ADD ./ .

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt \
    && pip install --no-cache-dir -U "https://code.aliyun.com/wang0618/pywebio/repository/archive.zip?ref=dev" \
    && wget -O /bokeh_sampledata.zip "https://code.aliyun.com/wang0618/bokeh_sampledata/repository/archive.zip?ref=master" \
    && mkdir -p ~/.bokeh \
    && unzip -d ~/.bokeh /bokeh_sampledata.zip \
    && mv ~/.bokeh/bokeh_* ~/.bokeh/data \
    && rm /bokeh_sampledata.zip

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

EXPOSE 8080

CMD python run.py