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

    cursor = connector.cursor()
    cursor.execute("select `timestamp`, `device_id`, `temperature` from temperatures")

    disp  = "<table>"
    disp += "<tr><th>date</th><th>ID</th><th>temperature</th></tr>"
    
    for row in cursor.fetchall():
        disp += "<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</td></tr>"
    
    disp += "</table>"
    
    cursor.close

    return "DB "+disp

@route('/input_temp')
def input_temp():
    # input temperatures
    cursor = connector.cursor()
    cursor.execute("INSERT INTO `temperatures` (`timestamp`, `device_id`, `temperature`) VALUES (NOW(), 1, 30.5)")

    # commit
    connector.commit();

    cursor.close

    return "SUCCESS"

@route('/test')
def test():
    # input temperatures
    device_id = request.query.device_id
    temperature = request.query.temperature

    cursor = connector.cursor()
    cursor.execute("INSERT INTO `temperatures` (`timestamp`, `device_id`, `temperature`) VALUES (NOW(), %s, %s)", (device_id,temperature))

    # commit
    connector.commit();

    cursor.close

    return device_id + temperature


connector.close
