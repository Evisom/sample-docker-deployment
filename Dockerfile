FROM python:3.12

COPY src/* /app/
COPY requirements.txt /app/
WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT python main.py