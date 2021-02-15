# Builds an image starting with the Python 3.9 image
FROM python:3.9-slim

# Copies the requirements.txt in my dir into the Docker space
COPY requirements.txt requirements.txt

# Installs the python dependencies from requirements.txt
RUN pip install -r requirements.txt
