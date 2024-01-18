# FROM python:3.11-slim as Builder

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     postgresql-server-dev-all \
#     gcc \
#     libc-dev \
#     libpq5 

# RUN apt-get update && apt-get install -y tk


# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"


# COPY requirements.txt /app/requirements.txt
# RUN pip install --upgrade pip && pip install -r /app/requirements.txt
# Run pip install pydantic[email]
# RUN pip 


# COPY . /app


# FROM python:3.11-slim

# WORKDIR /app


# RUN apt-get update && apt-get install -y libpq5


# COPY --from=Builder /app/ .
# COPY --from=Builder /opt/venv /opt/venv

# ENV PATH="/opt/venv/bin:$PATH"

# ENTRYPOINT ["python", "main.py"]


# Builder stage
FROM python:3.11 as Builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-server-dev-all \
    gcc \
    libc-dev \
    libpq5 \
    tk  

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
    tk  

COPY --from=Builder /app/ .
COPY --from=Builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

ENTRYPOINT ["python", "main.py"]
