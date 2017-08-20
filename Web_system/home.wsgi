#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
application = bottle.default_app()

@bottle.route('/')
def home():
    return "apache and wsgi. sitting in a tree"
