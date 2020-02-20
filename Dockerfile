# TODO: replace with FROM python:alpine
FROM python:3.9-rc-alpine

COPY main.py sitemap.py requirements.txt ./
RUN apk add --no-cache gcc musl-dev libxslt-dev && pip3 install pip==20.0.2 && pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "./main.py"]
