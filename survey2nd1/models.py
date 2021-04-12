
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
    # 1. Background
    s11_gender = models.CharField(
        choices=[['female', 'Kvinde'],
                 ['male', 'Mand']
                 ],
        verbose_name='Køn:',
        widget=widgets.RadioSelect()
    )

    s12_age = models.PositiveIntegerField(verbose_name='Alder:')

    s13_live_status = models.CharField(
        choices=[['alone', 'Jeg bor alene'],
                 ['with_partner', 'Je bor med min partner'],
                 ['with_partner_and_children', 'Jeg bor med min partner og børn'],
                 ['with_children', 'Jeg bor med mine børn'],
                 ],
        verbose_name='Hvordan bor du:',
        widget=widgets.RadioSelect()
    )

    s14_monthly_income = models.CharField(
        choices=[['above_40k', '40.000DKK eller over'],
                 ['between', 'Mellem 25.000DKK and 40.000DKK'],
                 ['less_25k', '25.000DKK eller under'],
                 ],
        verbose_name='Månedlig bruttoløn (før skat):',
        widget=widgets.RadioSelect()
    )

    s15_municipality = models.CharField(verbose_name='Hvilken kommune er du bosat i:')

    s16_property_ownership = models.CharField(
        choices=[['own', 'Ejerbolig'],
                 ['rent', 'Leje'],
                 ['others', "Andet"],
                 ],
        verbose_name='Hvordan vil du beskrive din bolig ejerforhold?',
        widget=widgets.RadioSelect()
    )

    s17_is_flood_risk_zone = models.CharField(
        choices=[['no', 'Nej. Ingen risiko'],
                 ['yes_medium', 'Ja. Mellem risiko'],
                 ['yes_high', 'Ja. Høj risiko']
                 ],
        verbose_name="Er din bolig i en oversvømmelsesrisikozone?",
        widget=widgets.RadioSelect()
    )

    s18_house_type = models.CharField(
        choices=[['duplex', 'Etagebolig'],
                 ['detached_house', 'Parcelhus'],
                 ['terraced_house', 'Rækkehus'],
                 ['others', 'Andet']
                 ],
        verbose_name = 'Hvordan vil du beskrive din boligtype?',
        widget=widgets.RadioSelect()
    )

    s19_is_exposed_climate_event = models.CharField(
        choices=[['yes', 'Ja'],
                 ['no', 'Nej']
                 ],
        verbose_name = 'Har du, et familiemedlem eller ven været udsat for klimarelateret begivenheder (f.eks. oversvømmelse)?',
        widget=widgets.RadioSelect()
    )

    s110_desc_climate_event = models.CharField(verbose_name='hvis ja, uddyb venligst:', blank=True, default='')

    s111_likelihood_climent_event = models.CharField(
        choices=[['highly unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly likely', 'højst sandsynligt']
                 ],
        verbose_name = 'Angiv, hvor sandsynligt du tror det ville være at blive udsat for ekstreme klimabegivenheder?',
        widget=widgets.RadioSelect()
    )

    s112_degree_or_disagree = models.CharField(
        choices=[['strongly agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['neither agree nor disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongly disagree', 'meget uenig'],
                 ],
        verbose_name='Vælg, hvor meget du er enig eller uenig i dette udsagn:\n Jeg har foretaget foranstaltninger for at mindske risikoen af at blive ramt af klimabegivenheder',
        widget=widgets.RadioSelect()
    )

######## 2. Economics History (DK)

    s21_prefered_option = models.CharField(
        choices=[['flatorcrown', 'Slå plat eller krone og vind 10.000 DKK med 50 procents sandsynlighed og 50 procents sandsynlighed for ingenting '],
                 ['win5kddk', 'Vind 5.000 DKK med sikkerhed'],
                 ['nomatter', 'Ligegyldigt, jeg synes begge muligheder er lige gode']
                 ],
        verbose_name='Hvilken mulighed ville du foretrække?',
        widget=widgets.RadioSelect()
    )

    s22_program_ab = models.CharField(
        choices=[['progA', 'Scenarie A: 200 mennesker bliver reddet med sikkerhed, de resterende 400 er for usikkert til at kunne komme med et estimat.'],
                 ['progB', 'Scenarie B: Der er en tredjedel (33,3%) sandsynlighed for, at 600 mennesker bliver reddet, og to tredjedels (66,6%) sandsynlighed for, at ingen mennesker bliver reddet.']
                 ],
        verbose_name='Hvilke af de to forslag vil du foretrække?',
        widget=widgets.RadioSelect()
    )

    s23_program_cd = models.CharField(
        choices=[['progC', 'Scenarie C: 400 mennesker vil omkomme med sikkerhed, de resterende 200 er for usikkert til at kunne komme med et estimat.'],
                 ['progD',
                  'Scenarie D: Der er en tredjedel (33,3%) sandsynlighed for, at ingen mennesker vil omkomme og to tredjedele (66,6%) sandsynlighed for, at 600 mennesker vil omkomme.']
                 ],
        verbose_name='Regeringen fremsætter to yderligere scenarier, hvilket vil du foretrække?',
        widget=widgets.RadioSelect()
    )

#####################
