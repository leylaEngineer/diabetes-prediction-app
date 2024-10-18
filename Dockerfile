# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

COPY ./static /app/static
COPY ./templates /app/templates

# Upgrade pip and setuptools
RUN pip install --upgrade pip==23.3 setuptools==70.0.0 scikit-learn==1.5.0
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and model
COPY . .

# Expose the port your app runs on
EXPOSE 80

# Command to run the application
CMD ["python", "app.py"]