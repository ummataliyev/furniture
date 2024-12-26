# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that Django runs on
EXPOSE 8000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED 1

# Run Django development server (adjust this for production if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
