# Dockerfile, Image, Container
FROM python:3.8

ADD DBOn.py .

RUN pip install pandas

CMD [ "python", "./DBOn.py"]

