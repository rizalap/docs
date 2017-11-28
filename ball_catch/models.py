from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Lingbo Huang'

doc = """
Ball-Catching Task
"""


class Constants(BaseConstants):
    name_in_url = 'ball_catch'
    players_per_group = None
    num_rounds = 6

    prize_and_cost = [1, 2, 3, 4, 5, 6]

class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            for p in self.get_players():
                my_prize_and_cost = Constants.prize_and_cost.copy()
                random.shuffle(my_prize_and_cost)
                p.participant.vars['my_prize_and_cost'] = my_prize_and_cost

        for p in self.get_players():
            p.condition = p.participant.vars['my_prize_and_cost'][self.round_number - 1]
            if p.condition <= 3:
                p.prize = 10
                p.cost = 5 * (p.condition - 1)
            else:
                p.prize = 20
                p.cost = 5 * (p.condition - 4)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    condition = models.IntegerField()
    prize = models.IntegerField()
    cost = models.IntegerField()

    catches = models.IntegerField()
    clicks = models.IntegerField()
    score = models.IntegerField()
    expense = models.IntegerField()

    def set_payoff(self):
        self.payoff = self.score - self.expense
