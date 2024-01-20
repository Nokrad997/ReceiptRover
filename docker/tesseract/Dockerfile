# Użyj oficjalnego obrazu Pythona jako obrazu bazowego
FROM python:3.11-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiuj pliki wymagań i zainstaluj zależności
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Zainstaluj Tesseract
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install opencv-python-headless
# Skopiuj resztę kodu źródłowego do kontenera
COPY . .

# Ustawienie zmiennej środowiskowej
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

# Ustawienie komendy, która uruchomi się podczas startu kontenera

CMD ["python", "/app/src/ocrapi/OCRService.py"]
