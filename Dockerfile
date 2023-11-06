FROM python:3.10-bookworm

COPY pages /app/
COPY tests /app/
COPY conftest.py /app/
COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

RUN pytest --alluredir=report_results

CMD ["allure", "serve", "/app/report_results", "--port", "9000"]
