from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def vars_for_template(self):
        intro_text = "ball_catch3/Instructions.html"

        if self.round_number > 1 and self.player.id_in_group == 2 :
            intro_text="ball_catch3/Instructions_2.html"

        return {
            'introduction': intro_text,
        }

class Task(Page):
    form_model = models.Player
    form_fields = ['catches', 'clicks', 'score', 'expense']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {
            'prize': self.player.prize,
            'cost': self.player.cost,
        }

    def before_next_page(self):
        self.player.set_payoff()

class firstphase(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number == 1


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.choose_2()
        self.group.set_payoff()
        for p in self.group.get_players():
            p.set_payoff()



class Results(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2


page_sequence = [
    Introduction,
    firstphase,
    Task,
    ResultsWaitPage,
    Results
]
