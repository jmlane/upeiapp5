#!/usr/bin/env python
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
import re

class MainHandler(webapp.RequestHandler):
    def get(self):

        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


class Fig35_1718Handler(webapp.RequestHandler):
    def get(self):

        template_values = {}

        path = os.path.join(os.path.dirname(__file__), 'fig35_1718.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        # the regular expression for matching most US phone numbers.
        telephoneExpression = re.compile(r'^\(\d{3}\)\d{3}-\d{4}$')

        template_values = {
                    'firstName' : self.request.get('firstname'),
                    'lastName' : self.request.get('lastname'),
                    'email' : self.request.get('email'),
                    'phone' : self.request.get('phone'),
                    'book' : self.request.get('book'),
                    'os' : self.request.get('os')
        }

        for key, value in template_values.iteritems():
            if value == '':
                template_values['printFormError'] = True
                break

        if not telephoneExpression.match(template_values['phone']):
            template_values['printPhoneError'] = True

        path = os.path.join(os.path.dirname(__file__), 'fig35_1718_post.html')
        self.response.out.write(template.render(path, template_values))


def main():
    application = webapp.WSGIApplication([
        ('/', MainHandler),
        ('/fig35_1718', Fig35_1718Handler)],
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
