#creating an docker base image for running python application
FROM python:3.10

#creating an container for images
COPY . /application

#assigning the containers as working directory
WORKDIR /application

#Adding the dependencies to the working directory
RUN pip install -r requirements.txt

#adding the command that run the server application
CMD python app.py