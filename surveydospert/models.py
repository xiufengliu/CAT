from otree.api import (
    models, widgets, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    BaseConstants)
import numpy as np
import time
import datetime as dt
from datetime import datetime

from .config import Constants
from otree.api import Currency as c

author = 'Xiufeng Liu (xiuli@dtu.dk)'

doc = """ N/A """


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    session_name = models.StringField()
    exec_time = models.StringField()

    def creating_session(self):
        self.session_name = self.session.config['name']
        self.exec_time = datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
#         'gender',
#         'age',
#         'live_status',
#         'monthly_income',
#         'municipality',
#         'property_ownership',
#         'is_flood_risk_zone',
#         'house_type',
#         'is_exposed_climate_event',
#         'desc_climate_event',
#         'likelihood_climent_event',
#         'degree_or_disagree',
#         'prefered_option',
#         'prog_AB',
#         'prog_CD'
# ******************************************************************************************************************** #

class Player(BasePlayer):
    q1 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'],
                 [2, '2 = meget lidt risiko'],
                 [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'],
                 [5, '5 = allerhøjest risiko']],
        widget=widgets.RadioSelect()
    )

    q2 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'],
                 [2, '2 = meget lidt risiko'],
                 [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'],
                 [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())

    q3 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'],
                 [2, '2 = meget lidt risiko'],
                 [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'],
                 [5, '5 = allerhøjest risiko']],
        widget=widgets.RadioSelect())
    q4 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'],
                 [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'],
                 [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q5 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q6 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q7 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q8 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q9 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q10 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q11 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q12 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q13 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q14 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q15 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q16 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q17 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q18 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q19 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q20 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q21 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q22 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q23 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q24 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q25 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q26 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q27 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q28 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q29 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q30 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q31 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q32 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q33 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q34 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
    q35 = models.PositiveIntegerField(
        choices=[[1, '1 = slet ikke risikofyldt'], [2, '2 = meget lidt risiko'], [3, '3 = nogen risiko'],
                 [4, '4 = høj risiko'], [5, '5 = allerhøjest risiko']], widget=widgets.RadioSelect())
