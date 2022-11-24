# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

RUN apt update
RUN apt-get -y install nginx && service nginx start
COPY ./nginx_conf/app_nginx.conf /etc/nginx/sites-enabled/
RUN apt install systemctl && systemctl enable nginx
#RUN service nginx restart


# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . app
WORKDIR /app


RUN python ./manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000
EXPOSE 80

# runs the production server
#ENTRYPOINT ["uwsgi", "./manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]
