FROM python:latest

WORKDIR /app

COPY requirement.txt /app
RUN pip install -r requirement.txt 

COPY . /app

EXPOSE 5000

CMD ["python","app.py","runserver","--host=0.0.0.0","--threaded"]

