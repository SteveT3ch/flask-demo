Demo Project
============

![Docker Compose](https://raw.githubusercontent.com/Stevet3ch/flask-demo/master/docker_logo.png?raw=true)

Demo project to learn the fundamental of using git and docker in a real project
[create a link to google](http://www.google.com)

Showing code `circleci.yml` with __backticks__.



##### DockerFile

```
  FROM python:3.5
  RUN apt-get update && apt-get install -qq -y build-essential libpq-dev --fix-missing --no-install-recommends
  RUN useradd -ms /bin/bash admin
  WORKDIR /app

  COPY requirements.txt requirements.txt
  RUN pip install -r requirements.txt
  USER admin
  CMD gunicorn -b 0.0.0.0:8000 "app:app"
```

Installation and docs
----------------------
- Full doc available in demo repo
- Contact developer for issues
- Code is maintain by Steve Peters

Contributing
-----------------------
![Build Status](https://circleci.com/gh/SteveT3ch/dockerapp2.svg?style=shield&circle-token=7b4e6d5a21bbe95e06b109bca9f5896ca6975516)  

Help is alway welcome - contact developer  

Releasing
------------------------
Releases are built by maintainer
