from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'rizal adi prima'

doc = """
create a random number to be seen by participant
"""


class Constants(BaseConstants):
    name_in_url = 'random_number_edit'
    players_per_group = None
    num_rounds = 1
    multiplier = 10
    endowment = 100

class Subsession(BaseSubsession):
    randnumber_edit = models.FloatField()

    def is_displayed(self):
        return self.player.id_in_group == 1

    def before_session_starts(self):
        for player in self.get_players():
            randnumber_edit = random.randint(1, 4)
            allocation_edit = models.PositiveIntegerField()
            player.participant.vars['randnumber_edit']=randnumber_edit
            player.participant.vars['allocation_edit']=allocation_edit




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
