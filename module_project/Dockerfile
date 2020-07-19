FROM python:3.7
WORKDIR /root/module_project
COPY ./ /root/module_project
RUN apt-get update -y; apt-get upgrade -y; apt-get install -y ssh mysql-client
# COPY ./run.sh /run.sh
# RUN chmod +x /run.sh
# CMD ["python", "main.py"]