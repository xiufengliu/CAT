from __future__ import division

from otree.common import safe_json

from . import models
from ._builtin import Page
from .models import Constants
import random, time
from otree.api import  Currency as c

# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #


def vars_for_all_templates(self):
    return {'round_no': self.round_number,
            'next_round_no': self.round_number + 1}


class Instr(Page):
    def vars_for_template(self):
        print('>>>Instr::vars_for_template')
        rnd = random.Random(time.time_ns())
        self.player.risk = rnd.choice(Constants.risks)
        return {'risk': self.player.risk}


class PayoffInfo(Page):
    def vars_for_template(self):
        print('>>>PayoffInfo::vars_for_template')
        #risk  = self.session.vars['control_risks'][self.round_number-1]
        return {'payoff_when_flood_without_adapt' : c(50),
                'total_payoff': c(Constants.stakes),
                'payoff_with_adapt': c(300)
                }



class Choice(Page):
    form_model = models.Player
    form_fields = [
        'adapt',
    ]

    def vars_for_template(self):
        print('>>>Choice::vars_for_template')
        return {'risk' : self.player.risk}


# ******************************************************************************************************************** #
# *** CLASS BOMB RISK ELICITATION TASK *** #
# ******************************************************************************************************************** #
class Bomb(Page):

    form_model = models.Player
    form_fields = [
        'hit_bomb',
    ]

    def is_displayed(self):
        #return self.player.adapt == 0
        return True

    def vars_for_template(self):
        print('>>>Bomb::vars_for_template')
        otree_vars = {
            'num_rows':      Constants.num_rows,
            'num_cols':      Constants.num_cols,
            'box_width':     Constants.box_width,
            'box_height':    Constants.box_height,
            'num_bombs':     self.player.risk
        }
        return {'otree_vars': safe_json(otree_vars)}

    def before_next_page(self):
        self.player.set_payoff()

# ******************************************************************************************************************** #
# *** CLASS RESULTS *** #
# ******************************************************************************************************************** #
class Results(Page):

    def is_displayed(self):
        return self.round_number==Constants.num_rounds

    def vars_for_template(self):
        print('>>>Results::vars_for_template')
        result = [{
                   'round_no' : index+1,
                    'risk' : p.risk,
                   'adapt' : 'Y' if p.adapt==1 else 'N',
                   'flood' : 'Y' if p.hit_bomb==1 else 'N',
                   'payoff' : p.payoff}
                  for index, p in enumerate(self.player.in_all_rounds())]
        results = self.participant.vars.get('results', [])
        results.append(result)
        self.participant.vars['results'] = results
        return {
                'result': result,
                'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()])}

# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [ Instr, Choice, Bomb, Results]
