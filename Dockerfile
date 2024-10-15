# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py.py main.py  # Replace with the name of your script

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the script
CMD ["python", "main.py"]  # Replace with the name of your script
