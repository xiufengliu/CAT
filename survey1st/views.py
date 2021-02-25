from __future__ import division


from . import models
from ._builtin import Page


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #

class SurveyQuestions(Page):
    form_model = models.Player
    form_fields = [
        'gender',
        'age',
        'nationality',
        'live_status',
        'monthly_income',
        'street_name',
        'post_code',
        'property_ownership',
        'flood_risk',
        'apartment_type',
        'risk_opt_preference',
        'frame_loss_aversion',
        'q1',
        'q2',
        'q3',
        'q4'
    ]

    def vars_for_template(self):
        return {'total_payoff': self.participant.payoff}

page_sequence = [SurveyQuestions]
