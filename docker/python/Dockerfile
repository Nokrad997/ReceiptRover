FROM python:3.11 as Builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-server-dev-all \
    gcc \
    libc-dev \
    libpq5 \
    tk \
    xvfb

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN pip install pydantic[email]

COPY . /app




# Final stage
FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    tk \
    xvfb

COPY --from=Builder /app/ .
COPY --from=Builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# Start virtual X server and run the application
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 -ac & python main.py"]

