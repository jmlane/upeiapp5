#!/usr/bin/env python
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
import re
from models.models import MailingList
from google.appengine.ext import db
import urllib

class MainHandler(webapp.RequestHandler):
    '''Handler for landing page of application.'''
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

class ListFormHandler(webapp.RequestHandler):
    '''Handler for the mailing list registration form page.'''

    @staticmethod
    def valid_form(form_dict):
        for key, value in form_dict.iteritems():
            if value == '':
                return False
        return True

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'form.html')
        self.response.out.write(template.render(path, {}))


    def post(self):
        # the regular expression for matching most US phone numbers.
        telephoneExpression = re.compile(r'^\(\d{3}\)\d{3}-\d{4}$')

        template_values = {
                    'first_name' : self.request.get('first_name'),
                    'last_name' : self.request.get('first_name'),
                    'email' : self.request.get('email'),
                    'phone' : self.request.get('phone'),
                    'book' : self.request.get('book'),
                    'bookurl' : urllib.quote(self.request.get('book')),
                    'os' : self.request.get('os')
        }

        if not self.valid_form(template_values):
            template_values['printFormError'] = True
        elif not telephoneExpression.match(template_values['phone']):
            template_values['printPhoneError'] = True
        else:
            form = MailingList(
                    first_name = self.request.get('first_name'),
                    last_name = self.request.get('last_name'),
                    email = self.request.get('email'),
                    phone = self.request.get('phone'),
                    book = self.request.get('book'),
                    os = self.request.get('os'))
            form.put()

        path = os.path.join(os.path.dirname(__file__), 'register.html')
        self.response.out.write(template.render(path, template_values))


class ShowListHandler(webapp.RequestHandler):
    '''Provides Handler for showlist page.'''
    def get(self):
        book = self.request.get('book')
        template_values = {}

        if not book == '':
            query = db.Query(MailingList)
            query.filter('book =', book)
            template_values['book'] = book
            template_values['results'] = [result for result in query]

        path = os.path.join(os.path.dirname(__file__), 'showlist.html')
        self.response.out.write(template.render(path, template_values))


class ShowAllHandler(webapp.RequestHandler):
    '''Provides handler for the showall page.'''
    def get(self):
        query = db.Query(MailingList)

        template_values = { 'results': [result for result in query] }

        path = os.path.join(os.path.dirname(__file__), 'showall.html')
        self.response.out.write(template.render(path, template_values))


def main():
    application = webapp.WSGIApplication([
        ('/', MainHandler),
        ('/form.html', ListFormHandler),
        ('/showlist.html', ShowListHandler),
        ('/showall.html', ShowAllHandler)],
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
