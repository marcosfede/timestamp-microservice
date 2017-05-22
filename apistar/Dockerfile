FROM python:latest
EXPOSE 8000
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
ADD . /code/
CMD gunicorn app:app.wsgi --workers=1 --bind=0.0.0.0:8000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
