#!/usr/bin/env python
import os
from google.appengine.ext.webapp import template

def render(page, template_values={}):
    '''Nice wrapper function for GAE template.render method.'''
    path = os.path.join(os.path.dirname(__file__), 'templates/', page)
    return template.render(path, template_values)
