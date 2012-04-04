from google.appengine.ext import db

class Users(db.Model):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    created_on = db.DateProperty(auto_now_add=True)

class TwitterAccounts(db.Model):
    screen_name = db.StringProperty(required=True)
    id = db.IntegerProperty(required=True)
    name = db.StringProperty()
    description = db.StringProperty()
    location = db.StringProperty()
    url = db.LinkProperty()

    @property
    def mentions(self):
        return Tweets.filter('mentions =', self.key())

class Tweets(db.Model):
    author = db.ReferenceProperty(TwitterAccounts,
                                  collection_name='tweets')
    body = db.StringProperty(required=True)
    in_reply_to = db.SelfReferenceProperty(collection_name='replies')
    mentions = db.ListProperty(db.Key)
    geo = db.GeoPtProperty()
