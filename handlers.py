#!/usr/bin/env python
from google.appengine.ext import webapp

class HomeHandler(webapp.RequestHandler):
    '''RequestHandler subclass for the home page.'''
    def get(self):
        self.response.out.write('See datastore admin for now.')

class TestHandler(webapp.RequestHandler):
    '''Handles generating test data and running test suite.'''
    def get(self):
        pass
