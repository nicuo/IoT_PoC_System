#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
connector = mysql.connector.connect (
            user     = 'root',
            password = 'mysql',
            host     = '172.17.0.2',
            database = 'db1'
)

from bottle import (
    run,
    route,
    request,
    default_app
)
application = default_app()

@route('/')
def home():
    return "Display temperature on web board"

@route('/list')
def list():
    """list temperature from DB"""

    # select  all data from DB
    cursor = connector.cursor()
    cursor.execute("select `timestamp`, `device_id`, `temperature` from temperatures")

    # shaping all data
    disp  = "<table>"
    disp += "<tr><th>date</th><th>ID</th><th>temperature</th></tr>"
    
    for row in cursor.fetchall():
        disp += "<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</td></tr>"
    
    disp += "</table>"
    
    # close
    cursor.close

    return "DB "+disp

@route('/input_temp')
def input_temp():
    """input temperature to DB """

    # set temperature variables
    device_id = request.query.device_id
    temperature = request.query.temperature

    # insert into temperatures
    cursor = connector.cursor()
    cursor.execute("INSERT INTO `temperatures` (`timestamp`, `device_id`, `temperature`) VALUES (NOW(), %s, %s)", (device_id,temperature))

    # commit and close
    connector.commit();
    cursor.close

    return "SUCCESS"

@route('/clear')
def clear():
    """ clear all data at temperatures table """

    # clear all data
    cursor = connector.cursor()
    cursor.execute("TRUNCATE TABLE temperatures")

    # commit and close
    connector.commit();
    cursor.close

    return "SUCCESS"


connector.close
