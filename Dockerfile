FROM python:3.5
RUN apt-get update && apt-get install -qq -y build-essential libpq-dev --fix-missing --no-install-recommends
RUN useradd -ms /bin/bash admin
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#COPY app /app
USER admin
CMD gunicorn -b 0.0.0.0:8000 "app:app"
