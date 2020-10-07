# Use an existing docker image as a base
FROM python:3.8

# set the working directory in the container
# (when downloads the image it automatically starts from that directory)
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .


# # Download and install a dependency
RUN pip install -r requirements.txt

# COPY DJANGO PROJECT
COPY project_urls . 

# Tell the image what to do when
# it starts as a container
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
