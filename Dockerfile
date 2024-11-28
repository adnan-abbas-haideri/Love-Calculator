# Use the official Python 3.11 image with Bullseye
FROM python:3.11-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the host to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the default command to run the app
CMD ["python", "app.py"]

