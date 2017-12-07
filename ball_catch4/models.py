from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Lingbo Huang wtih some commits from Rizal adi prima'

doc = """
Ball-Catching Task
"""


class Constants(BaseConstants):
    name_in_url = 'ball_catch4'
    players_per_group = 2
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

    total_catch = models.IntegerField()
    average = models.IntegerField()

    def in_round(self,roundnumber):
        players = self.get_players()
        self.total_catch=sum([p.catches for p in self.get_players()if p.catches is not None])
        average=(self.total_catch)/len(players)
        self.average=round(average,2)
        self.session.vars['avgcatch'] = self.average



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
        self.ballcatch = self.catches*1
        self.participant.vars['income1'] = self.payoff
        self.participant.vars['catches1']= self.ballcatch