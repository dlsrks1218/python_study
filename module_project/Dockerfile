FROM python:3.7

WORKDIR /root/module_project

COPY ./__init__.py /root/module_project
COPY ./main.py /root/module_project
COPY ./module.py /root/module_project
COPY ./db_module.py /root/module_project
COPY ./requirements.txt /root/module_project

RUN apt-get update -y; apt-get upgrade -y;
RUN apt-get install -y mysqlclient
RUN pip install -r requirements.txt
# CMD ["python", "main.py"]