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
    name_in_url = 'random_number1'
    players_per_group = None
    num_rounds = 1
    multiplier = 10

class Subsession(BaseSubsession):
    randnumber1 = models.FloatField()

    def before_session_starts(self):
        for player in self.get_players():
            randnumber1 = random.randint(1, 4)
            player.participant.vars['randnumber1']=randnumber1

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
