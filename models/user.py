from protorpc import messages
from google.appengine.ext import ndb


class User(ndb.Model):
    """User profile"""
    name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    wins = ndb.IntegerProperty(default = 0)
    total_played = ndb.IntegerProperty(default = 0)
    score = ndb.IntegerProperty(default = 0)

  
