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
    name_in_url = 'ball_catch3'
    players_per_group = None
    num_rounds = 2

    prize_and_cost = [1, 2, 3, 4]

class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            for p in self.get_players():
                my_prize_and_cost = Constants.prize_and_cost.copy()
                random.shuffle(my_prize_and_cost)
                p.participant.vars['my_prize_and_cost'] = my_prize_and_cost

        for p in self.get_players():
            p.condition = p.participant.vars['my_prize_and_cost'][self.round_number - 1]
            if p.condition <= 2:
                p.prize = 10
                p.cost = 5 * (p.condition - 1)
            else:
                p.prize = 20
                p.cost = 5 * (p.condition - 2)


class Group(BaseGroup):

    def set_payoff(self):
        players = self.get_players
        total_catch=[p.catches for p in players]
        average=sum(total_catch)/len(players)
        self.average=round(average,2)
        self.session.vars['avgcatch'] = self.average



class Player(BasePlayer):

    condition = models.IntegerField()
    prize = models.IntegerField()
    cost = models.IntegerField()
    catches = models.IntegerField()
    clicks = models.IntegerField()
    score = models.IntegerField()
    expense = models.IntegerField()
    total_catch = models.IntegerField()
    average = models.IntegerField()

    def set_payoff(self):
        self.payoff = self.score - self.expense
        self.ballcatch = self.catches*1
        self.participant.vars['income1'] = self.payoff
        self.participant.vars['catches1']= self.ballcatch
