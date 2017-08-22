#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
connector = mysql.connector.connect (
            user     = 'root',
            password = 'mysql',
            host     = '172.17.0.3',
            database = 'test'
)

import bottle
application = bottle.default_app()

@bottle.route('/')
def home():
    return "apache and wsgi. sitting in a tree"

@bottle.route('/input_temp')
def input_temp():
    # input temperatures
    cursor = connector.cursor()
    cursor.execute("INSERT INTO `temperatures` (`temperature`, `update_time`) VALUES (" + request.query.temp + ", NOW() )")

    # commit
    connector.commit();

    cursor.close

    return "SUCCESS"

#　close connector 
connector.close
