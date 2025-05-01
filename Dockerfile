# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables (optional here, handled in Docker run or Kubernetes)
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]
