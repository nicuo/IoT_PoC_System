#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
connector = mysql.connector.connect (
            user     = 'root',
            password = 'mysql',
            host     = '172.17.0.2',
            database = 'db1'
)

import bottle
application = bottle.default_app()

@bottle.route('/')
def home():
    return "apache and wsgi. sitting in a tree"

@bottle.route('/list')
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

@bottle.route('/input_temp')
def input_temp():
    # input temperatures
    device_id = 1
    temerature = 30.5
    cursor = connector.cursor()
    #cursor.execute("INSERT INTO `temperatures` (`temperature`, `update_time`) VALUES (" + request.query.temp + ", NOW() )")
    #cursor.execute("INSERT INTO `temperatures` (`timestamp`, `device_id`, `temperature`) VALUES (NOW() " + device_id + ", " + temperature + ")")
    cursor.execute("INSERT INTO `temperatures` (`timestamp`, `device_id`, `temperature`) VALUES (NOW(), 1, 30.5)")

    # commit
    connector.commit();

    cursor.close

    return "SUCCESS"

#　close connector 
connector.close
