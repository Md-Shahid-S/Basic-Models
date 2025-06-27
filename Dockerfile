# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all other source code
COPY . .

# Expose port (Flask default)
EXPOSE 5000

# Run using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
