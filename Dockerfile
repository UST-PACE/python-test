FROM python:3.9
#debugging
RUN ls -altr .
RUN pwd

COPY requirements.txt .

WORKDIR /script

#COPY requirements.txt .

RUN pip install -r requirements.txt

COPY batch_processor.py .

ENTRYPOINT [ "python", "batch_processor.py"]