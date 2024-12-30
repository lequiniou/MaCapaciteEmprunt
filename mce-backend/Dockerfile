# Use the official Python image as the base image
FROM python:3.10-slim

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that FastAPI uses
EXPOSE 8000

# Set environment variables
ENV POSTGRES_HOST=host.docker.internal \
    POSTGRES_PORT=5432 \
    POSTGRES_DB=mce_db \
    POSTGRES_USER=mcebackend \
    POSTGRES_PASSWORD=mcebackendpass 
# !!! passing the password this way causes security issues, secrets manager should be used instead !!!

# Command to run the application
CMD ["bash", "launch_app.sh"]