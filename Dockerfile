FROM python:3.9

#debugging
RUN ls -altr .

WORKDIR workspace
RUN ls -altr .

COPY requirements.txt /script

WORKDIR /script

#COPY requirements.txt .
RUN pip install -r requirements.txt

COPY batch_processor.py .

ENTRYPOINT [ "python", "batch_processor.py"]