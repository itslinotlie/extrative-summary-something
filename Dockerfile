# Builds an image starting with the Python 3.9 image
# According to guides, -slim tag points to a minimum Debian installation 
# (aka might need to install additonal tools yourself)
FROM python:3.9-slim

# Copies the requirements.txt in my dir into the Docker space
COPY requirements.txt requirements.txt

# Installs the python dependencies from requirements.txt
RUN pip install -r requirements.txt

# to have docker running without it closing asap, use "docker run -it <repo>:<tag>"
# use tag --rm to delete conatiner after use for good practice and to save space
# https://realpython.com/python-versions-docker/ actually helpful website