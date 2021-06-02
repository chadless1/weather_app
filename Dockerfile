#Create a ubuntu base image with python 3 installed.
FROM python:3.8

#Set the working directory
WORKDIR /weather_app

#copy all the files
COPY . .

#Install the dependencies
RUN pip3 install -r requirements.txt

#Run the command
CMD ["python3", "app.py"]
