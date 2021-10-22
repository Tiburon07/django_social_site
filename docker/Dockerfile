FROM python:latest
COPY etc/apt/sources.list /etc/apt/sources.list
# CONFIGURA TZDATA
RUN ln -fs /usr/share/zoneinfo/Europe/Rome /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

# INSTALLA DIPENDENZE
RUN apt update
RUN apt upgrade -y
RUN apt install default-libmysqlclient-dev git -y
RUN git clone https://github.com/alranel/django-bootstrap-italia
WORKDIR django-bootstrap-italia
RUN python setup.py install
RUN pip install django==3.2.8 mysqlclient django-ajax-datatable design-django-theme

# ESEGUI DJANGO
WORKDIR /app
CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8080"]
