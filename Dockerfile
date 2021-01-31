FROM python:3.7-alpine


RUN python3 -m pip install --upgrade pip

RUN pip install -U setuptools

RUN apk update

RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev openssl-dev libffi-dev g++ git && \
    python3 -m pip install -r requirements.pip --no-cache-dir && \
    apk --purge del .build-deps




ENTRYPOINT [ "/bin/sh", "/launch.sh" ]