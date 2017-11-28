from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def vars_for_template(self):
        intro_text = "ball_catch2/Instructions.html"

        if self.round_number > 1:
            intro_text="ball_catch2/Instructions_2.html"

        return {
            'introduction': intro_text,
        }

class Task(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
        }

    def before_next_page(self):
        self.player.set_payoff()



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Task,
    ResultsWaitPage,
    Results
]
