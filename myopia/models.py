
from otree.api import (
    models, widgets, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    BaseConstants)
import numpy as np
import time
from .config import Constants

author = 'Xiufeng Liu (xiuli@dtu.dk)'

doc = """ N/A """




# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def before_session_starts(self):
        np.random.seed(int(time.time()))
        risk = np.random.choice(Constants.risks, Constants.players_per_group)
        self.session.vars['myopia_risks'] = [risk]*Constants.num_rounds

# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass



# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    hit_bomb = models.PositiveIntegerField(initial=0)
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
