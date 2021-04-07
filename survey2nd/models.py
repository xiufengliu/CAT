
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
                 ['yes', 'Ja. Høj risiko']
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


######## 3. Sense of coherence soc (DK)
    s31_findsolution = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg er i stand til at finde løsninger på problemstillinger, som opstår i min hverdag.',
        widget=widgets.RadioSelect()
    )
    s32_findvalue = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg er i stand til at finde værdi i selve håndtering af de problemstillinger, som jeg står over for i min hverdag.',
        widget=widgets.RadioSelect()
    )
    s33_understand_issue = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg er i stand til at forstå og forudsige de problemstillinger, som opstår i min hverdag.',
        widget=widgets.RadioSelect()
    )

######## 4. Community of coherence SOC (DK)
    s41_adversity = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='De vil overkomme de udfordringer, som følger af oversvømmelsen.',
        widget=widgets.RadioSelect()
    )
    s42_staycalm = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='De vil bevare roen, imens de vil tage stilling til hvad de skal gøre.',
        widget=widgets.RadioSelect()
    )
    s43_meaning_exp = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='De vil finde mening i oplevelsen.',
        widget=widgets.RadioSelect()
    )


######## 5. DOMAIN-SPECIFIC RISK-TAKING SCALE DOSPERT (DK)
    s51_diff_taste = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… indrømme, at du har en anderledes smag end dine venner?',
        widget=widgets.RadioSelect()
    )

    s52_camping = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… campere ude i vildmarken?',
        widget=widgets.RadioSelect()
    )
    s53_beghorseracing = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… satse en dagløn på hestevæddeløb?',
        widget=widgets.RadioSelect()
    )
    s54_investfund = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… investere 10% af din årsløn i en pensionsfond?',
        widget=widgets.RadioSelect()
    )
    s55_drinking = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… drikke store mængder alkohol ved et socialt arrangement?',
        widget=widgets.RadioSelect()
    )
    s56_taxdeduction = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… angive et lidt for højt fradrag til SKAT?',
        widget=widgets.RadioSelect()
    )
    s57_disagreeauth = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… erklære dig uenig med en autoritet, hvad angår et vigtigt emne?',
        widget=widgets.RadioSelect()
    )
    s58_stakepokergame = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… satse en dagløn på et pokerspil med høje indsatser?',
        widget=widgets.RadioSelect()
    )
    s59_affair = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… have en affære med en gift person?',
        widget=widgets.RadioSelect()
    )
    s510_takecredit = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… tage æren for en anden persons arbejde?',
        widget=widgets.RadioSelect()
    )
    s511_rundownski = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?',
        widget=widgets.RadioSelect()
    )
    s512_invest5perincome = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… investere 5% af din årsindtægt i en stærkt spekulativ aktie?',
        widget=widgets.RadioSelect()
    )
    s513_whitewaterrafting = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… tage på white water rafting om foråret når strømmen er stærkest?',
        widget=widgets.RadioSelect()
    )
    s514_wageonmatch = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)?',
        widget=widgets.RadioSelect()
    )
    s515_unsupportedsex = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… dyrke ubeskyttet sex?',
        widget=widgets.RadioSelect()
    )
    s516_revealsecret = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… røbe en vens hemmelighed til en anden person?',
        widget=widgets.RadioSelect()
    )
    s517_drivecarnobelt = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… køre i bil uden sele?',
        widget=widgets.RadioSelect()
    )
    s518_investstartup = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… investere 10% af din årsindtægt i en nystartet virksomhed?',
        widget=widgets.RadioSelect()
    )
    s519_learnparachute = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… lære at springe i faldskærm?',
        widget=widgets.RadioSelect()
    )
    s520_ridemoto = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… køre på motorcykel uden hjelm?',
        widget=widgets.RadioSelect()
    )
    s521_choosecareer = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?',
        widget=widgets.RadioSelect()
    )
    s522_sayunpopularcase = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… sige hvad du mener om en upopulær sag til et møde på arbejdet?',
        widget=widgets.RadioSelect()
    )

    s523_sunbathe = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… tage solbad uden solcreme?',
        widget=widgets.RadioSelect()
    )

    s524_jumpbungee = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… springe bungy-jump fra en høj bro?',
        widget=widgets.RadioSelect()
    )

    s525_takesmallplane = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… flyve en lille flyvemaskine?',
        widget=widgets.RadioSelect()
    )

    s526_gohomealone = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… gå alene hjem om natten gennem et af byens farlige kvarterer?',
        widget=widgets.RadioSelect()
    )
    s527_movetofarawaycity = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… flytte til en by langt væk fra din familie?',
        widget=widgets.RadioSelect()
    )
    s528_startnewcareer = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name="… påbegynde en ny karriere midt i 30'erne?",
        widget=widgets.RadioSelect()
    )
    s529_leavekidathome = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… efterlade dine små børn alene hjemme, imens du løber et ærinde?',
        widget=widgets.RadioSelect()
    )
    s530_keeppurse = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… beholde en pung du har fundet, som indeholder 1.000 kroner?',
        widget=widgets.RadioSelect()
    )

    s531_movehouse = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… flytte til et hus, som ligger langs bredden af en flod:',
        widget=widgets.RadioSelect()
    )
    s532_sendkidtoschool = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… sende børn i skolen, imens DMI varsler om farligt vejr i dit område:',
        widget=widgets.RadioSelect()
    )
    s533_drivefloodedroad = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… køre på en oversvømmet vej.',
        widget=widgets.RadioSelect()
    )
    s534_parkcar = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.',
        widget=widgets.RadioSelect()
    )
    s535_hiking = models.CharField(
        choices=[['highly_unlikely', 'højst usandsynligt'],
                 ['unlikely', 'usandsynligt'],
                 ['not_certain', 'ikke sikkert'],
                 ['likely', 'sandsynligt'],
                 ['highly_likely', 'højst sandsynligt'],
                 ],
        verbose_name='… tage på vandreture, imens DMI varsler om farligt vejr i området.',
        widget=widgets.RadioSelect()
    )

    ### 6.FLOOD DOMAIN-SPECIFIC RISK-TAKING SCALE F-DOSPERT
    s61_diff_taste = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… indrømme, at du har en anderledes smag end dine venner?',
        widget=widgets.RadioSelect()
    )

    s62_camping = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… campere ude i vildmarken?',
        widget=widgets.RadioSelect()
    )
    s63_beghorseracing = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… satse en dagløn på hestevæddeløb?',
        widget=widgets.RadioSelect()
    )
    s64_investfund = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… investere 10% af din årsløn i en pensionsfond?',
        widget=widgets.RadioSelect()
    )
    s65_drinking = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… drikke store mængder alkohol ved et socialt arrangement?',
        widget=widgets.RadioSelect()
    )
    s66_taxdeduction = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… angive et lidt for højt fradrag til SKAT?',
        widget=widgets.RadioSelect()
    )
    s67_disagreeauth = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… erklære dig uenig med en autoritet hvad angår et vigtigt emne?',
        widget=widgets.RadioSelect()
    )
    s68_stakepokergame = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… satse en dagløn på et pokerspil med høje indsatser?',
        widget=widgets.RadioSelect()
    )
    s69_affair = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… have en affære med en gift person?',
        widget=widgets.RadioSelect()
    )
    s610_takecredit = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… tage æren for en anden persons arbejde?',
        widget=widgets.RadioSelect()
    )
    s611_rundownski = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?',
        widget=widgets.RadioSelect()
    )
    s612_invest5perincome = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… investere 5% af din årsindtægt i en stærkt spekulativ aktie?',
        widget=widgets.RadioSelect()
    )
    s613_whitewaterrafting = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… tage på white water rafting om foråret når strømmen er stærkest?',
        widget=widgets.RadioSelect()
    )
    s614_wageonmatch = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)??',
        widget=widgets.RadioSelect()
    )
    s615_unsupportedsex = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… dyrke ubeskyttet sex?',
        widget=widgets.RadioSelect()
    )
    s616_revealsecret = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… røbe en vens hemmelighed til en anden person?',
        widget=widgets.RadioSelect()
    )
    s617_drivecarnobelt = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… køre i bil uden sele?',
        widget=widgets.RadioSelect()
    )
    s618_investstartup = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… investere 10% af din årsindtægt i en nystartet virksomhed?',
        widget=widgets.RadioSelect()
    )
    s619_learnparachute = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… lære at springe i faldskærm?',
        widget=widgets.RadioSelect()
    )
    s620_ridemoto = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… køre på motorcykel uden hjelm?',
        widget=widgets.RadioSelect()
    )
    s621_choosecareer = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?',
        widget=widgets.RadioSelect()
    )
    s622_sayunpopularcase = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… sige hvad du mener om en upopulær sag til et møde på arbejdet?',
        widget=widgets.RadioSelect()
    )

    s623_sunbathe = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… tage solbad uden solcreme?',
        widget=widgets.RadioSelect()
    )

    s624_jumpbungee = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… springe bungy-jump fra en høj bro?',
        widget=widgets.RadioSelect()
    )

    s625_takesmallplane = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… flyve en lille flyvemaskine?',
        widget=widgets.RadioSelect()
    )

    s626_gohomealone = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… gå alene hjem om natten gennem et af byens farlige kvarterer?',
        widget=widgets.RadioSelect()
    )
    s627_movetofarawaycity = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… flytte til en by langt væk fra din familie?',
        widget=widgets.RadioSelect()
    )
    s628_startnewcareer = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name="… påbegynde en ny karriere midt i 30'erne?",
        widget=widgets.RadioSelect()
    )
    s629_leavekidathome = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… efterlade dine små børn alene hjemme, imens du løber et ærinde?',
        widget=widgets.RadioSelect()
    )
    s630_keeppurse = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… beholde en pung du har fundet, som indeholder 1.000 kroner?',
        widget=widgets.RadioSelect()
    )

    s631_movehouse = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… flytte til et hus beliggende langs bredden af en flod:',
        widget=widgets.RadioSelect()
    )
    s632_sendkidtoschool = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… sende børn i skolen, imens DMI varsler om farligt vejr i dit område:',
        widget=widgets.RadioSelect()
    )
    s633_drivefloodedroad = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… køre på en oversvømmet vej.',
        widget=widgets.RadioSelect()
    )
    s634_parkcar = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.',
        widget=widgets.RadioSelect()
    )
    s635_hiking = models.CharField(
        choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'],
                 ['Very_little_risk', 'Meget lidt risiko'],
                 ['No_risk', 'Nogen risiko'],
                 ['High_risk', 'Høj risiko'],
                 ['Very_high_risk', 'Allerhøjest risiko'],
                 ],
        verbose_name='… tage på vandreture, imens DMI varsler om farligt vejr i området.',
        widget=widgets.RadioSelect()
    )


    #### 7. PERSONALITY INVENTORY HEXACO - BHI (DK)

    s71_lookpainting = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg kan se på et maleri i lang tid.',
        widget=widgets.RadioSelect()
    )
    s72_thingsinplace = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg sørger for, at mine ting altid er på deres plads.',
        widget=widgets.RadioSelect()
    )
    s73_remainunkind = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg forbliver uvenlig overfor nogen, som har været ondsindet overfor mod mig.',
        widget=widgets.RadioSelect()
    )
    s74_nobodylikeme = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Ingen kan lide at tale  med mig.',
        widget=widgets.RadioSelect()
    )
    s75_afraidfeelingpain = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg er bange for at føle smerte.',
        widget=widgets.RadioSelect()
    )
    s76_hardtolie = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg har svært ved at lyve.',
        widget=widgets.RadioSelect()
    )
    s77_sciboring = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg synes, at videnskab er kedeligt.',
        widget=widgets.RadioSelect()
    )
    s78_postponetask = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg udskyder indviklede opgaver så længe som muligt',
        widget=widgets.RadioSelect()
    )
    s79_criticism = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg giver ofte kritik.',
        widget=widgets.RadioSelect()
    )
    s710_gettouchstranger = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg har let ved at tage kontakt til fremmede.',
        widget=widgets.RadioSelect()
    )
    s711_worry = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg bekymrer mig mindre end andre.',
        widget=widgets.RadioSelect()
    )
    s712_wondering = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg gad godt vide, hvordan man på uærlig vis kan tjene en masse penge.',
        widget=widgets.RadioSelect()
    )
    s713_goodimg = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg har en god fantasi.',
        widget=widgets.RadioSelect()
    )
    s714_precise = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg arbejder meget præcist.',
        widget=widgets.RadioSelect()
    )
    s715_agreeothers = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg enes hurtigt med andre.',
        widget=widgets.RadioSelect()
    )
    s716_talkothers = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg kan lide at snakke med andre.',
        widget=widgets.RadioSelect()
    )
    s717_overcome = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg overvinder let problemer på egen hånd.',
        widget=widgets.RadioSelect()
    )
    s718_famous = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg vil gerne være berømt.',
        widget=widgets.RadioSelect()
    )
    s719_lovepeople = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg elsker mennesker med mærkelige idéer.',
        widget=widgets.RadioSelect()
    )
    s720_dothings = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg gør ofte ting uden rigtigt at tænke.',
        widget=widgets.RadioSelect()
    )
    s721_staycalm = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Selv når jeg bliver behandlet dårligt, forbliver jeg rolig.',
        widget=widgets.RadioSelect()
    )
    s722_wellmanner = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg  er sjældent veloplagt.',
        widget=widgets.RadioSelect()
    )
    s723_tear = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg fælder en tåre, når jeg ser sørgelige eller romantiske film.',
        widget=widgets.RadioSelect()
    )
    s724_soap = models.CharField(
        choices=[['strongly_agree', 'meget enig'],
                 ['agree', 'enig'],
                 ['n_agree_disagree', 'hverken enig eller uenig'],
                 ['disagree', 'uenig'],
                 ['strongdisagree', 'meget uenig'],
                 ],
        verbose_name='Jeg har krav på særbehandling.',
        widget=widgets.RadioSelect()
    )
    ################email#####
    email = models.CharField(verbose_name='E-mail:', blank=True, default='')
#####################
