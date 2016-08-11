from protorpc import messages
from google.appengine.ext import ndb
import pickle


class Game(ndb.Model):
    """Game object"""
    user = ndb.KeyProperty(required=True, kind = 'User')
    game_over = ndb.BooleanProperty(required = True, default = False)
    survived = ndb.BooleanProperty(required = True, default = False)
    canceled_game = ndb.BooleanProperty(required = True, default=False)
    history = ndb.PickleProperty(required = True)
    game_started = ndb.BooleanProperty(required = True, default=False)
    difficulty = ndb.IntegerProperty(required = True, default=1)
    timeout = ndb.BooleanProperty(required = True, default=False)
    timer = ndb.IntegerProperty(required = True, default=0)
    

