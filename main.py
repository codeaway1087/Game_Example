import logging
import webapp2
from google.appengine.api import mail, app_identity
from google.appengine.ext import ndb
from api import SurviveAPI
from utils import get_by_urlsafe
from models.user import User
from models.game import Game




app = webapp2.WSGIApplication([
    ('/tasks/send_newgame_email', SendNewGameEmail), ('/cron/send_reminder',\
     ReminderEmail)], debug=True)
