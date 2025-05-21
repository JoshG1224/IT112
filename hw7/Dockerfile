# Use a slim Python image
FROM python:3.11-slim

# Avoid creating .pyc files and force terminal output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files into container
COPY . /app/

# Open port 8000 and run Django server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
