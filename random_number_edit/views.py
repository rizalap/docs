from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    pass

class MyPage(Page):
    def vars_for_template(self):
       return {'randnumber_edit': self.player.participant.vars['randnumber_edit'],'allocation_edit':self.player.participant.vars['randnumber_edit']*10,}

    def is_displayed(self):
        return self.player.id_in_group == 1

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass
    def vars_for_template(self):
        if self.player.id_in_group == 2:
            body_text = "You are The Receiver. Waiting for the random number generator shown to your co-player (the Sender) to decide."
        else:
            body_text = 'Please wait'
        return {'body_text': body_text}


class Results(Page):
    pass

page_sequence = [
    Instructions,
    MyPage,
    ResultsWaitPage
]
