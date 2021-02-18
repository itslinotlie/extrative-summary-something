# I think I finally understand why people always download a linux image ->
# because then you can "use the terminal" with the commands and what not.
# Just need to also download python + pip to download packages
# and run python <file name> and then you'll be able
# to run the python script. Only took a couple hours for this realization -.-
FROM debian:latest

# apt-get update downlaods downloads+updates packages
# the -y flag in apt-get install forces the answer "yes" to the question
# "are you sure you want to install this package"
# downloading python + pip because this is a python project. Took a while to realize
# I needed python3 and python3-pip rather than normal python and python-pip ):
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Not exactly sure if this is needed, but just in case, this upgrades
# pip to the latest version
RUN pip3 install --upgrade pip

# Copies my entire directory into the docker container (which is why .dockerignore is a thing)
COPY . .

# Installs the python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# to have docker running without it closing asap, use "docker run -it <repo>:<tag>"
# use tag --rm to delete conatiner after use for good practice and to save space (i.e. -it --rm)
# https://realpython.com/python-versions-docker/ actually helpful website
# run exit in the terminal to exit from the terminal (wow shocker, but I didn't know that)

# to build a docker image, use "docker built -t <name>:<tag>" and magic will happen