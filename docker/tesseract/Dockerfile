FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
EXPOSE 5000
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install opencv-python-headless

COPY . .

ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata
RUN apt-get update && apt-get install -y tesseract-ocr-pol
ENV FLASK_APP="/app/src/ocrapi/OCRService.py"

HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]