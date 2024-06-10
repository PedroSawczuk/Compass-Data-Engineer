FROM python:3.7-slim

RUN pip install boto3 python-dotenv

WORKDIR /app

COPY data-code.py .

COPY data/movies.csv /data/movies.csv
COPY data/series.csv /data/series.csv

COPY .env .

CMD ["python", "data-code.py"]
