# Use an official Python runtime as the base image
FROM python:3.11.5-slim

# Set environment variables
ENV APP_HOME /assignment1
ENV PORT 5000

# Create the application directory
WORKDIR $APP_HOME

# Copy the application files into the created directory
COPY app.py requirements.txt linear_regression_model.joblib ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE $PORT

# Command to run the Flask application
CMD ["python", "app.py"]
