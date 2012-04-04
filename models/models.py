#!/usr/bin/env python
from google.appengine.ext import db

class MailingList(db.Model):
    '''Defines the HRD Model for the assignment 2 mailing list.'''
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    phone = db.PhoneNumberProperty(required=True)
    book = db.StringProperty(required=True, choices=set(
        ['XML How to Program',
         'Python How to Program',
         'E-business and E-commerce How to Program',
         'Internet and WWW How to Program 3e',
         'C++ How to Program 4e',
         'Java How to Program 5e',
         'Visual Basic How to Program'
        ]))
    os = db.StringProperty(required=True, choices=set(
        ['Windows XP',
         'Windows 2000',
         'Windows 95_98',
         'Linux',
         'Other'
        ]))
