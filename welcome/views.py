from __future__ import division

from otree.common import safe_json

from . import models
from ._builtin import Page
from .models import Constants
from otree.api import  Currency as c

# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #

# ******************************************************************************************************************** #
# *** CLASS BOMB RISK ELICITATION TASK *** #
# ******************************************************************************************************************** #

class Welcome(Page):

    def vars_for_template(self):
        return {'change_rate': '{} = {}'.format(c(60), c(60).to_real_world_currency(self.session)),
                'image_path': 'welcome/images/welcome.png'}

page_sequence = [ Welcome]
