FROM python:latest

RUN pip install flask
RUN pip install flask_restplus

ADD main.py .

EXPOSE 80

CMD ["python","main.py"]