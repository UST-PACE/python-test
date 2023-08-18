FROM python:3.8
#debugging
RUN ls -altr .
RUN pwd
RUN ls -altr bin
WORKDIR workspace
RUN pwd
RUN ls -altr .

COPY requirements.txt /script

WORKDIR /script

#COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY batch_processor.py .

ENTRYPOINT [ "python", "batch_processor.py"]