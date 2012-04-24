#!/usr/bin/env python
from google.appengine.ext import webapp
from helpers import render

class HomeHandler(webapp.RequestHandler):
    '''RequestHandler subclass for the home page.'''

    def get(self):
        self.response.out.write(render('home.html'))

class TestHandler(webapp.RequestHandler):
    '''Handles generating test data and running test suite.'''

    def get(self):
        values = { 'header': 'Test page'}
        self.response.out.write(render('test.html', values))
