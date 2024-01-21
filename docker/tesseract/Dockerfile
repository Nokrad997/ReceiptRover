FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install -y tesseract-ocr-pol
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install opencv-python-headless

COPY . .


FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /usr/local /usr/local

ENV PATH="/usr/local/bin/python:${PATH}"
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

 

ENV FLASK_APP="/app/src/ocrapi/OCRService.py"

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
