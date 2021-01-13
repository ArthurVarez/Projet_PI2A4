FROM python:latest


WORKDIR /app

COPY requirement.txt /app
RUN pip install -r requirement.txt 

COPY . /app

ENV FLASK_APP=app.py

EXPOSE 5050 


CMD ["python","app.py"]