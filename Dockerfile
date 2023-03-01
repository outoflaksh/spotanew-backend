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

# Expose port 8000 for the FastAPI app and 6379 for Redis
EXPOSE 8000 6379

# Set the entrypoint to start the app
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
