from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    created_on = db.DateProperty(auto_now_add=True)

class TwitterAccount(db.Model):
    screen_name = db.StringProperty(required=True)
    id = db.IntegerProperty(required=True)
    name = db.StringProperty()
    description = db.StringProperty(multiline=True)
    location = db.StringProperty(multiline=True)
    url = db.LinkProperty()

    @property
    def mentions(self):
        return Tweet.filter('mentions =', self.key())

class Tweet(db.Model):
    author = db.ReferenceProperty(TwitterAccount,
                                  collection_name='tweets')
    text = db.StringProperty(required=True)
    in_reply_to = db.SelfReferenceProperty(collection_name='replies')
    mentions = db.ListProperty(db.Key)
    created_at = db.DateProperty()
    geo = db.GeoPtProperty()
