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
            wget\
            apache2\
            libapache2-mod-wsgi
RUN pip install bottle
RUN wget https://pypi.python.org/packages/59/e0/775bf5fb3dd4c7f9aa6877907d4a96eecca6886c603dedfea6e843e94560/mysql-connector-2.1.6.tar.gz#md5=cd197b038754a7dddf266de5f6bb8ab4
RUN tar -zxvf mysql-connector-2.1.6.tar.gz
WORKDIR mysql-connector-2.1.6
RUN python ./setup.py build
RUN python ./setup.py install

# STEP:2 start apache server
#ADD ./index.html /var/www/html/
ADD ./home.wsgi /var/www/html/
RUN sed -i -e "\#DocumentRoot /var/www/html#a WSGIScriptAlias / /var/www/html/home.wsgi" /etc/apache2/sites-available/000-default.conf
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D", "FOREGROUND"]
