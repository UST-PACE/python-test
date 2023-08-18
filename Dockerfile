FROM python:3.9

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY batch_processor.py /app

# EXPOSE 8080
ENTRYPOINT [ "python", "batch_processor.py"]