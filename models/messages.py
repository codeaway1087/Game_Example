from protorpc import messages
from user import (
	UserForm,
	ScoreForm
	)




class ScoreForms(messages.Message):
    items = messages.MessageField(ScoreForm, 1, repeated = True)
