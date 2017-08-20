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
            apache2\
            libapache2-mod-wsgi
RUN pip install bottle

# STEP:2 start apache server
#ADD ./index.html /var/www/html/
ADD ./home.wsgi /var/www/html/
RUN sed -i -e "\#DocumentRoot /var/www/html#a WSGIScriptAlias / /var/www/html/home.wsgi" /etc/apache2/sites-available/000-default.conf
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D", "FOREGROUND"]
