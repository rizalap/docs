from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

"""


class Constants(BaseConstants):
    name_in_url = 'mydictator_example'
    players_per_group = 2
    num_rounds = 1


    # Initial amount allocated to the dictator
    endowment = c(100)

    kept_choices = range (10, 100, 10)

    multiplier=2
    offer_increment = c(10)

    offer_choices = currency_range(10, endowment, offer_increment)


class Player(BasePlayer):
    color = models.CharField()
    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        if self.id_in_group == 2:
            return 'receiver'

class Subsession(BaseSubsession):

    def before_session_starts(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


def question(amount):
    return 'How much do you think the sender will offer to you if the random number was showing the number of {}?'.format(
        c(amount))

"""""""""
 only if we random the assignment to be executed for each round
    def before_session_starts(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['color'] = random.choice(['blue', 'red'])

 --> only if we want to have it multiple round
   def before_session_starts(self):
       if self.round_number == 1:
           paying_round = random.randint(1, Constants.num_rounds)
       self.session.vars['paying_round'] = paying_round
        if self.round_number == 3:
            # reverse the roles
            for group in self.get_groups():
                players = group.get_players()
                players.reverse()
                group.set_players(players)
        if self.round_number > 3:
            self.group_like_round(3)
"""""""""

class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""Amount sender decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='I will keep (from 0 to %i)' % Constants.endowment
    )

    Ikeep = models.CurrencyField (
        choices=Constants.kept_choices,
        doc="""receiver kept""",
        verbose_name='I understand that the amount of random number advise me to allocate this amount',
        widget=widgets.RadioSelectHorizontal()
    )

    # for strategy method
    response_10 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(10))
    response_20 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(20))
    response_30 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(30))
    response_40 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(40))
    response_50 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(50))
    response_60 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(60))
    response_70 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(70))
    response_80 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(80))
    response_90 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(90))
    response_100 = models.CharField(
        choices=[None, '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(100))


    def set_payoffs(self):
        sender = self.get_player_by_id(1)
        receiver = self.get_player_by_id(2)
        if self.round_number == 1:
            sender.payoff = self.kept * 2
            receiver.payoff = Constants.endowment - self.kept
        if self.round_number == 2:
            sender.payoff = self.kept
            receiver.payoff = (Constants.endowment - self.kept) * 2






