#!/usr/bin/env python
from google.appengine.ext import webapp
from models import TwitterAccount
from helpers import render

class HomeHandler(webapp.RequestHandler):
    '''RequestHandler subclass for the home page.'''

    def get(self):
        self.response.out.write(render('home.html'))


class ListHandler(webapp.RequestHandler):
    '''Handles the generation of list pages.'''

    def get(self, path):
        if path == '/people':
            at = int(self.request.get('at') or 0)
            by = int(self.request.get('by') or 10)

            if at:
                query = TwitterAccount.all().order('screen_name')
                query = query.filter('__key__ >', at)
            else:
                query = TwitterAccount.all().order('screen_name')
            query = query.fetch(by)

            values = { 'people': [p for p in query],
                       'title': 'List of people'
            }

            self.response.out.write(render('list-people.html', values))

        else:
            values = {
                'error': '<strong>Warning:</strong> page unavailable.',
                'message': 'This list page is not yet implemented.'
            }
            self.response.out.write(render('error.html', values))


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
        values = {
            'error': '<strong>Warning:</strong> OAuth '
                'login did not complete.',
            'message': 'OAuth is not yet implemented correctly. This '
                'is a placeholder for the appropriate handler.'
        }

        self.response.out.write(render('error.html', values))
        return


class TestHandler(webapp.RequestHandler):
    '''Handles generating test data and running test suite.'''

    def get(self):
        values = { 'header': 'Test page'}
        self.response.out.write(render('test.html', values))
