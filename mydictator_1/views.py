from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        intro_text = "mydictator_1/Instructions.html"

        if self.player.id_in_group > 1:
            intro_text= "mydictator_1/Instructions_2.html"

        return {
            'introduction': intro_text,
            'allocation1': self.player.participant.vars['randnumber1'] * 10,
        }

    timeout_seconds = 120


class Instructions :
    pass

class Offer(Page):
    form_model = models.Group
    form_fields = ['kept','Ikeep']

    def vars_for_template(self):
        return {'allocation1': self.player.participant.vars['randnumber1'] * 10,
        }

    def is_displayed(self):
        return self.player.id_in_group == 1

    timeout_seconds = 120

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        if self.player.id_in_group == 2:
            body_text = "You are participant 2. Waiting for participant 1 to decide."
        else:
            body_text = 'Please wait'
        return {'body_text': body_text}


class Results(Page):
    def offer(self):
        return (Constants.endowment - self.group.kept)*2

    def vars_for_template(self):
        return {
            'offer': (self.group.kept)*3,
            'receiver_offer' : Constants.endowment - self.group.kept,
            'offer2':self.group.kept,
            'receiver_offer2': (Constants.endowment - self.group.kept)*3,
        }


page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results
]