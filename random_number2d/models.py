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
    name_in_url = 'random_number2c'
    players_per_group = None
    num_rounds = 1
    multiplier = 10
    endowment = 100

class Subsession(BaseSubsession):
    randnumber = models.FloatField()

    def is_displayed(self):
        return self.player.id_in_group == 1

    def before_session_starts(self):
        for player in self.get_players():
            randnumber2c = random.randint(1, 10)
            player.participant.vars['randnumber2c']=randnumber2c




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
