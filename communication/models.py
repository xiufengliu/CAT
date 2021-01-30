
from otree.api import (
    models, widgets, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    BaseConstants)
import random
import time


from .config import Constants

author = 'Xiufeng Liu (xiuli@dtu.dk)'

doc = """ N/A """




# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    session_name = models.StringField()
    def creating_session(self):
        rnd = random.Random(time.time_ns())
        self.session.vars['communication_risks'] = [rnd.choices(Constants.risks, k=Constants.players_per_group) for i in range(Constants.num_rounds)]
        self.session_name = self.session.config['name']





# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass



# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    hit_bomb = models.PositiveIntegerField()
    group_adapt = models.PositiveIntegerField(
        choices=[[1, 'Yes'],
                 [0, 'No']
                 ],
        widget=widgets.RadioSelect()
    )

    adapt = models.PositiveIntegerField(
        choices=[[1, 'Yes'],
                 [0, 'No']
                 ],
        widget=widgets.RadioSelect()
    )

    risk = models.PositiveIntegerField()

    def set_payoff(self):
        if self.group_adapt:
            self.payoff = 400
        else:
            if self.adapt==1:
                self.payoff = 300
            else:
                if self.hit_bomb==1:
                    self.payoff = 50
                else:
                    self.payoff = Constants.stakes

