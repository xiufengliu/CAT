
from otree.api import (
    models, widgets, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    BaseConstants)
import numpy as np
import time
import datetime as dt
from datetime import datetime


from .config import Constants
from otree.api import  Currency as c
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
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    gender = models.CharField(
        choices=[['female', 'Female'],
                 ['male', 'Male']
                 ],
        verbose_name='Please state your gender:',
        widget=widgets.RadioSelect()
    )

    age = models.PositiveIntegerField(verbose_name='Please state your age:')

    nationality = models.CharField(verbose_name='What is your nationality?')

    live_status = models.CharField(
        choices=[['alone', 'I live alone'],
                 ['with_partner', 'I live with my partner'],
                 ['with_partner_and_children', 'I live with my partner and children'],
                 ['others', 'Others'],
                 ],
        verbose_name='Please state your living status:',
        widget=widgets.RadioSelect()
    )

    monthly_income = models.CharField(
        choices=[['40k_above', '40,000DKK and above'],
                 ['between', 'Between 25,000DKK and 40,000DKK'],
                 ['less_25k', '25,000DKK and less'],
                 ],
        verbose_name='Please state your monthly gross income:',
        widget=widgets.RadioSelect()
    )


    street_name = models.CharField(verbose_name='What is the name of your street?')


    post_code = models.CharField(verbose_name='Please fill the post code:')

    property_ownership = models.CharField(
        choices=[['own', 'Own'],
                 ['rent', 'Rent'],
                 ['live_at_relative_residence', "Living at relatives' residence"],

                 ],
        verbose_name='Do you own or rent your current property?',
        widget=widgets.RadioSelect()
    )

    flood_risk = models.CharField(
        choices=[['no_risk', 'No risk'],
                 ['high_risk', 'High risk']
                 ],
        verbose_name="What is your residence's flood risk zone?",
        widget=widgets.RadioSelect()
    )

    apartment_type = models.CharField(
        choices=[['an_apartment', 'An apartment'],
                 ['a_house', 'A house']
                 ],
        verbose_name = 'What is your dwelling type?',
        widget=widgets.RadioSelect()
    )

    risk_opt_preference = models.CharField(
        choices=[['toss_a_coin', 'Toss a coin, win {} with probability of 0.5 and win nothing with probability of 0.5'.format(c(10000))],
                 ['win_5k_tokens', 'Win {} with certainty'.format(c(5000))],
                 ['either', 'Either, I am indifferent to the two options']
                 ],
        verbose_name = 'Which option do you prefer?',
        widget=widgets.RadioSelect()
    )

    frame_loss_aversion = models.CharField(
        choices=[['risk_averse_in_gains', 'Program A: 200 people will be saved;  Program  B: There is a one-third probability that 600 people will be saved,and a two-thirds probability that no people will be saved'],
                 ['risk_loving_in_losse', 'Program C: 400 people will die; Program D: There is a one-third probability that nobody will die, and a two-third probability that 600 people will die']
                 ],
        verbose_name = 'Which of the two programs would you favor?',
        widget=widgets.RadioSelect()
    )

    q1 = models.PositiveIntegerField(
        choices=[[1, '{} immediately'.format(c(300))],
                 [0, '{} in two months'.format(c(500))]
                 ],
        verbose_name='What would you prefer?',
        widget=widgets.RadioSelect()
    )
    q2 = models.PositiveIntegerField(
        choices=[[1, '{} in one year'.format(c(300))],
                 [0, '{} in one year and two months'.format(c(500))]
                 ],
        verbose_name='What would you prefer?',
        widget=widgets.RadioSelect()
    )

    q3 = models.PositiveIntegerField(
        choices=[[1, '{} tokens in one year and two months'.format(c(400))],
                 [0, 'Being able to choose, one year from today, {} then {} in two months'.format(c(300), c(500))]
                 ],
        verbose_name='What would you prefer?',
        widget=widgets.RadioSelect()
    )

    q4 = models.PositiveIntegerField(
        choices=[[1, '{} in one year and two months'.format(c(700))],
                 [0, 'Being able to choose, one year from today, {} then {} in two months'.format(c(300), c(500))]
                 ],
        verbose_name='What would you prefer?',
        widget=widgets.RadioSelect()
    )

