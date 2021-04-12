from __future__ import division


from . import models
from ._builtin import Page


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
class Intro(Page):
    pass

class SQ1(Page):
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
        's112_degree_or_disagree']

class SQ2(Page):
    form_model = models.Player
    form_fields = [
        's21_prefered_option',
        's22_program_ab',
        's23_program_cd'
        ]
page_sequence = [Intro, SQ1, SQ2]

