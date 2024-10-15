# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and the script to the container
COPY requirements.txt requirements.txt
COPY main.py main.py 

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the script
CMD ["python", "main.py"]  # Ensure this matches the copied script name
