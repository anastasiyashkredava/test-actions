FROM python:3.10-bookworm

RUN pip install -r requirements.txt

COPY pages /app/
COPY tests /app/
COPY conftest.py /app/
COPY requirements.txt /app/

WORKDIR /app

CMD ["pytest"]
