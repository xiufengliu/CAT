from __future__ import division


from . import models
from ._builtin import Page


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #

class SurveyQuestions(Page):
    form_model = models.Player
    form_fields = [
        's11_gender',
        's12_age',
        's13_live_status',
        's14_monthly_income',
        's15_municipality',
        's16_property_ownership',
        's17_is_flood_risk_zone',
        's18_house_type',
        's19_is_exposed_climate_event',
        's110_desc_climate_event',
        's111_likelihood_climent_event',
        's112_degree_or_disagree',
        's21_prefered_option',
        's22_program_ab',
        's23_program_cd',
        's31_findsolution',
        's32_findvalue',
        's33_understand_issue'
    ]

    def vars_for_template(self):
        return dict(total_payoff=self.participant.payoff,
                    )

page_sequence = [SurveyQuestions]
