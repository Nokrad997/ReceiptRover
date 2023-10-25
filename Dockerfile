FROM python:3.11-alpine as Builder

RUN apk update && apk upgrade \
    && apk add --no-cache git

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY . /app

FROM python:3.11-alpine

WORKDIR /app
COPY --from=Builder /app/penis.py . 


ENTRYPOINT ["python", "penis.py"]