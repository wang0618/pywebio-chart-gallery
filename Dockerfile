FROM python:3

WORKDIR /usr/src/app

ADD ./ .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -U --force-reinstall pywebio

RUN pip freeze

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

EXPOSE 8080

CMD python run.py 8080
