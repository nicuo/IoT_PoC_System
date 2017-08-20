#STEP:0 Jessie(Base image)
FROM resin/rpi-raspbian:jessie
MAINTAINER Nicuo

#STEP:1 install things
RUN apt-get update && apt-get upgrade
RUN apt-get install -y\
            python\
            python-pip\
            python-dev\
            gcc\
            make\
            git\
            vim\
            apache2
RUN pip install bottle

# STEP:2 start apache server
ADD ./index.html /var/www/html/
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D", "FOREGROUND"]
