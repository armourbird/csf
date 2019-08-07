#Base image
FROM python:3.7.4-alpine

LABEL \
  name="csf-server" \
  version="1.0Beta" \
  github="https://github.com/armourbird/csf"

#Add CSF master
WORKDIR /root/CSF
COPY . /root/CSF

#Install python packages
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["/bin/sh", "./start.sh"]