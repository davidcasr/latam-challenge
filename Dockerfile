# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port that the app runs on
EXPOSE 8080

# Run the app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
