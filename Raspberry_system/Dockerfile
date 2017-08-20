#STEP:0 Jessie(Base image)
FROM resin/rpi-raspbian:jessie
MAINTAINER Nicuo

#STEP:1 install things
RUN apt-get update
RUN apt-get install -y\
            python\
            python-pip\
            python-dev\
            gcc\
            make\
            vim\
            git
RUN pip install rpi.gpio
RUN pip install pyserial

#STEP:2 do python file (. is Raspberry_system)
ADD ./python_arduino_ctrl.py /home
WORKDIR /home
ENTRYPOINT ["python","python_arduino_ctrl.py"]
