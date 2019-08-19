FROM python:3.7.4-buster

WORKDIR /app

COPY . /app

RUN pip install -r Requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]