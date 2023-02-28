# Specify the base image
FROM python:3.8-slim-buster

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the FastAPI app and 6379 for Redis
EXPOSE 8000 6379

# Set the entrypoint to start the app
COPY dev.entrypoint.sh /dev.entrypoint.sh
RUN chmod +x /dev.entrypoint.sh
ENTRYPOINT ["/dev.entrypoint.sh"]