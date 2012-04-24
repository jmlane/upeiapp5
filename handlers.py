#!/usr/bin/env python
from google.appengine.ext import webapp
from helpers import render

class HomeHandler(webapp.RequestHandler):
    '''RequestHandler subclass for the home page.'''

    def get(self):
        self.response.out.write(render('home.html'))


class LogInHandler(webapp.RequestHandler):
    '''RequestHandler instance for log-in page.'''

    def get(self):
        values = { 'title': 'Log-in' }

        self.response.out.write(render('login.html', values))

    def post(self):
        # Not implemented. Pass error.
        error = 'Traditional login not implemented. Please use Twitter \
                OAuth.'

        values = { 'title': 'Log-in' }
        if error:
            values['error'] = error

        self.response.out.write(render('login.html', values))


class LogInTwitterHandler(webapp.RequestHandler):
    def get(self):
        pass


class TestHandler(webapp.RequestHandler):
    '''Handles generating test data and running test suite.'''

    def get(self):
        values = { 'header': 'Test page'}
        self.response.out.write(render('test.html', values))
