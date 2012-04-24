#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers import HomeHandler, LogInHandler, TestHandler,\
    LogInTwitterHandler

def main():
    application = webapp.WSGIApplication(
            [('/', HomeHandler),
             ('/login', LogInHandler),
             ('/login/twitter', LogInTwitterHandler),
             ('/test', TestHandler)],
            debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
