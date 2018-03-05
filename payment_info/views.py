from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PaymentInfo(Page):

    def vars_for_template(self):
        result = []
        total_payoff = c(0)
        for phase_r in self.participant.vars.get('results'):
            phase_payoff = c(0)
            phase_no = None
            for round_r in phase_r:
                phase_no = round_r['phase_no']
                phase_payoff += round_r['payoff']
            result.append({'phase_no': phase_no, 'payoff': phase_payoff, 'payoff_c': phase_payoff.to_real_world_currency(self.session)})
            total_payoff += phase_payoff
        self.participant.payoff_in_real_world_currency = total_payoff.to_real_world_currency(self.session)
        return {
            'result': result,
            'total_payoff' : total_payoff,
            'total_payoff_c' : self.participant.payoff_plus_participation_fee()
            }

page_sequence = [PaymentInfo]
