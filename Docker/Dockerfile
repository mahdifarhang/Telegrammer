FROM python:3.10-slim

# Keeps the python output streams are sent to the terminal
# Check https://stackoverflow.com/a/59812588/7280058
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y locales iputils-ping net-tools gettext build-essential cron \
    && locale-gen en_US.UTF-8 \
    && pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -U pip \
    && pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir uwsgi psycopg2-binary \
 && apt-get clean

RUN mkdir /code
WORKDIR /code

ADD ./Docker/docker-entrypoint.sh /entrypoint.sh

## Install requirements
ADD ./requirements.txt /code/requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt
## Add code to container
ADD . /code

ENV UWSGI_UID=www-data UWSGI_GID=www-data
ENV LANG="en_US.UTF-8" 
ENV LANGUAGE="en_US.UTF-8"
ENV LC_ALL="en_US.UTF-8"
ENV ENTRYPINT_MODE uwsgi

# for uWSGI emperor mode
#RUN mkdir -p /etc/uwsgi/vassals
#RUN sudo ln -s /code/Deployment/uwsgi.ini /etc/uwsgi/vassals/

EXPOSE 8000

ENTRYPOINT ["bash","/entrypoint.sh"]
