# Use a stable Python base image (best for compatibility)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies (Flask, TensorFlow, Pillow, etc.)
# Using --no-cache-dir speeds up the installation process
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code (including app.py, monuments.py, templates/, and monument_model.h5)
COPY . /app

# Expose the standard port for Hugging Face Spaces when using Docker
EXPOSE 7860

# Command to run your application using Gunicorn (replacing the Procfile for Docker)
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:7860"]