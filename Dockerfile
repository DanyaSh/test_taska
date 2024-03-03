# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Configure Poetry
# Disable the creation of a virtual environment inside the Docker container since it's not required
RUN poetry config virtualenvs.create false

# Install project dependencies via Poetry without dev dependencies
RUN poetry install --no-dev

# Copy the rest of the project files
COPY . /app

# Define the command to run the application
#CMD ["poetry", "run", "python", "test_taska/main_polling.py"]
CMD ["poetry", "run", "python", "test_taska/main_webhook.py"]
