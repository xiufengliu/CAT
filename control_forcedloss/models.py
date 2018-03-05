
from otree.api import (
    models, widgets, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    BaseConstants)
import numpy as np
import random
from .config import Constants

author = 'Xiufeng Liu (xiuli@dtu.dk)'

doc = """ N/A """




# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.session.vars['control_risks'] = [np.random.choice(Constants.risks, Constants.players_per_group) for
                                                     i in range(Constants.num_rounds)]
        self.session.vars['must_hit'] = [random.randint(1, Constants.players_per_group) for
                                         i in range(Constants.num_rounds)]

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

    adapt = models.PositiveIntegerField(
        choices=[[1, 'Yes'],
                 [0, 'No']
                 ],
        widget=widgets.RadioSelect()
    )

    risk = models.PositiveIntegerField()

    def set_payoff(self):
        if self.adapt==1:
            self.payoff=300
        else:
            if self.hit_bomb==1:
                self.payoff = 50
            else:
                self.payoff = Constants.stakes
