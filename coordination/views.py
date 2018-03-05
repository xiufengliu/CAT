from __future__ import division

from otree.common import safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import numpy as np
from otree.api import  Currency as c
# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #


def vars_for_all_templates(self):
    phase_no = self.session.config['app_sequence'].index('coordination')
    return {'phase_no': phase_no}



class GroupInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1

class GroupInstr(Page):
    def is_displayed(self):
        return self.round_number == 1


class GroupChoice(Page):
    form_model = models.Player
    form_fields = [
        'group_adapt',
    ]

    def vars_for_template(self):
        coordination_risks = self.session.vars['coordination_risks'][self.round_number-1]
        risks = [coordination_risks[self.player.id_in_group - 1],]
        self.player.risk = risks[0]
        for player in self.group.get_players():
            if not player is self.player:
                risks.append(coordination_risks[player.id_in_group - 1])
        return {'risk0' : risks[0],
                'risk1': risks[1],
                'risk2': risks[2]}


class VotingWait(WaitPage):

    def after_all_players_arrive(self):
        group_adapt = 1
        for p in self.group.get_players():
            group_adapt = group_adapt and p.group_adapt

        for p in self.group.get_players():
            p.group_adapt = group_adapt

class SelfInstructions(Page):

    def is_displayed(self):
        return not self.player.group_adapt


class SelfChoice(Page):
    form_model = models.Player
    form_fields = [
        'adapt'
    ]

    def is_displayed(self):
        return not self.player.group_adapt

    def vars_for_template(self):
        self.player.risk = np.random.choice(Constants.risks)
        return {
            'risk': self.player.risk
        }


# ******************************************************************************************************************** #
# *** CLASS BOMB RISK ELICITATION TASK *** #
# ******************************************************************************************************************** #
class Bomb(Page):

    form_model = models.Player
    form_fields = [
        'hit_bomb',
    ]

    def is_displayed(self):
        return True
        #return not self.group.adapt

    def vars_for_template(self):
        otree_vars = {
            'num_rows':      Constants.num_rows,
            'num_cols':      Constants.num_cols,
            'box_width':     Constants.box_width,
            'box_height':    Constants.box_height,
            'num_bombs':     self.player.risk,
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
        phase_no = self.session.config['app_sequence'].index('coordination')
        result = [{'phase_no' : phase_no,
                   'round_no' : index+1,
                   'group_adapt' : 'Y' if p.group_adapt else 'N',
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
page_sequence = [GroupInstr,  GroupChoice, VotingWait, SelfInstructions, SelfChoice, Bomb, Results]
