from judge.forms import ProblemSubmitForm
from django.forms import CharField, HiddenInput
import json

class BetaProblemSubmitForm(ProblemSubmitForm):
    suspicious_behaviors = CharField(max_length=256, initial="[]", widget = HiddenInput())
    
