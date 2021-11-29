FROM python:3.8

RUN apt-get update

# Create the working directory
RUN mkdir /logs_generator
WORKDIR /logs_generator

# Copy data and python scripts from local to the working directory
COPY ./logs_generator/requirements.txt .
COPY ./logs/ ./data
COPY ./logs_generator/logs_producer.py . 

# Install python requirements
# RUN pip install -r requirements.txt

RUN pip install pandas
RUN pip install kafka-python

# Expose the python script on port
# EXPOSE 3333

# Run the python script
CMD ["python","-u","logs_producer.py"]