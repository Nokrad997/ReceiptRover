# Stage 1: Build stage
FROM python:3.11-slim as Builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-server-dev-all \
    gcc \
    libc-dev \
    libpq5

# Set up virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install required Python packages
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN pip 

# Copy the rest of the application
COPY . /app

# Stage 2: Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Install libpq5
RUN apt-get update && apt-get install -y libpq5

# Copy files from the build stage
COPY --from=Builder /app/ .
COPY --from=Builder /opt/venv /opt/venv

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"

ENTRYPOINT ["python", "penis.py"]
