from otree.api import (
    models, widgets, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
    BaseConstants)
import numpy as np
import time
from otreeutils.surveys import create_player_model_for_survey, generate_likert_field, generate_likert_table
from django.forms.widgets import Select
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

SURVEY_DEFINITIONS = {
    'SQ1': {
        'page_title': '1. BAGGRUNDSSPØRGSMÅL',
        'survey_fields': [
            ('s11_gender', {
                'text': 'Køn:',
                'field': generate_likert_field(['Kvinde', 'Mand'], choices_values=['female', 'male'],
                                               widget=widgets.RadioSelect())()
            }),
            ('s12_age', {
                'text': 'Alder:',
                'field': models.PositiveIntegerField(),
            }),
            ('s13_live_status', {
                'text': 'Hvordan bor du:',
                'field': generate_likert_field(
                    ['Jeg bor alene', 'Je bor med min partner', 'Jeg bor med min partner og børn',
                     'Jeg bor med mine børn'],
                    choices_values=['alone', 'with_partner', 'with_partner_and_children', 'with_children'],
                    widget=widgets.RadioSelect())()
            }),
            ('s14_monthly_income', {
                'text': 'Månedlig bruttoløn (før skat):',
                'field': models.CharField(
                    choices=[['above 40k', '40.000DKK eller over'],
                             ['between', 'Mellem 25.000DKK and 40.000DKK'],
                             ['less 25k', '25.000DKK eller under'],
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s15_municipality', {
                'text': 'Hvilken kommune er du bosat i:',
                'field': models.CharField()
            }),
            ('s16_property_ownership', {
                'text': 'Hvordan vil du beskrive din bolig ejerforhold?',
                'field': models.CharField(
                    choices=[['own', 'Ejerbolig'],
                             ['rent', 'Leje'],
                             ['others', "Andet"],
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s17_is_flood_risk_zone', {
                'text': "Er din bolig i en oversvømmelsesrisikozone?",
                'field': models.CharField(
                    choices=[['no', 'Nej. Ingen risiko'],
                             ['medium', 'Ja. Mellem risiko'],
                             ['high', 'Ja. Høj risiko']
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s18_house_type', {
                'text': 'Hvordan vil du beskrive din boligtype?',
                'field': models.CharField(
                    choices=[['duplex', 'Etagebolig'],
                             ['detached house', 'Parcelhus'],
                             ['terraced house', 'Rækkehus'],
                             ['others', 'Andet']
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s19_is_exposed_climate_event', {
                'text': 'Har du, et familiemedlem eller ven været udsat for klimarelateret begivenheder (f.eks. oversvømmelse)?',
                'field': models.CharField(
                    choices=[['yes', 'Ja'],
                             ['no', 'Nej']
                             ],
                    widget=widgets.RadioSelect()
                )

            }),
            ('s110_desc_climate_event', {
                'text': 'hvis ja, uddyb venligst:',
                'field': models.CharField(blank=True, default='')
            }),
            ('s111_likelihood_climent_event', {
                'text': 'Angiv, hvor sandsynligt du tror det ville være at blive udsat for ekstreme klimabegivenheder?',
                'field': models.CharField(
                    choices=[['highly unlikely', 'højst usandsynligt'],
                             ['unlikely', 'usandsynligt'],
                             ['not certain', 'ikke sikkert'],
                             ['likely', 'sandsynligt'],
                             ['highly likely', 'højst sandsynligt']
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s112_degree_or_disagree', {
                'text': 'Vælg, hvor meget du er enig eller uenig i dette udsagn:\n Jeg har foretaget foranstaltninger for at mindske risikoen af at blive ramt af klimabegivenheder',
                'field': models.CharField(
                    choices=[['strongly agree', 'meget enig'],
                             ['agree', 'enig'],
                             ['neutral', 'hverken enig eller uenig'],
                             ['disagree', 'uenig'],
                             ['strongly disagree', 'meget uenig'],
                             ],
                    widget=widgets.RadioSelect()
                )
            }),

        ]
    },
    'SQ2': {
        'page_title': '2. NOGLE UDGSAGN OM DIG',
        'survey_fields': [
            generate_likert_table(labels=['meget enig', 'enig', 'hverken enig eller uenig', 'uenig', 'meget uenig'],
                                  choices_values=['strongly agree', 'agree', 'neutral', 'disagree',
                                                  'strongly disagree'],
                                  questions=[
                                      ('s21_lookpainting', 'Jeg kan se på et maleri i lang tid.'),
                                      ('s22_thingsinplace', 'Jeg sørger for, at mine ting altid er på deres plads.'),
                                      ('s23_remainunkind',
                                       'Jeg forbliver uvenlig overfor nogen, som har været ondsindet overfor mod mig.'),
                                      ('s24_nobodylikeme', 'Ingen kan lide at tale  med mig.'),
                                      ('s25_afraidfeelingpain', 'Jeg er bange for at føle smerte.',),
                                      ('s26_hardtolie', 'Jeg har svært ved at lyve.'),
                                      ('s27_sciboring', 'Jeg synes, at videnskab er kedeligt.'),
                                      ('s28_postponetask', 'Jeg udskyder indviklede opgaver så længe som muligt'),
                                      ('s29_criticism', 'Jeg giver ofte kritik.'),
                                      ('s210_gettouchstranger', 'Jeg har let ved at tage kontakt til fremmede.'),
                                      ('s211_worry', 'Jeg bekymrer mig mindre end andre.'),
                                      ('s212_wondering',
                                       'Jeg gad godt vide, hvordan man på uærlig vis kan tjene en masse penge.'),
                                      ('s213_goodimg', 'Jeg har en god fantasi.'),
                                      ('s214_precise', 'Jeg arbejder meget præcist.'),
                                      ('s215_agreeothers', 'Jeg enes hurtigt med andre.'),
                                      ('s216_talkothers', 'Jeg kan lide at snakke med andre.'),
                                      ('s217_overcome', 'Jeg overvinder let problemer på egen hånd.'),
                                      ('s218_famous', 'Jeg vil gerne være berømt.'),
                                      ('s219_lovepeople', 'Jeg elsker mennesker med mærkelige idéer.'),
                                      ('s220_dothings', 'Jeg gør ofte ting uden rigtigt at tænke.'),
                                      ('s221_staycalm', 'Selv når jeg bliver behandlet dårligt, forbliver jeg rolig.'),
                                      ('s222_wellmanner', 'Jeg  er sjældent veloplagt.'),
                                      ('s223_tear', 'Jeg fælder en tåre, når jeg ser sørgelige eller romantiske film.'),
                                      ('s224_soap', 'Jeg har krav på særbehandling.')

                                  ],
                                  form_help_initial='<p>Angiv for hvert udsagn, hvorvidt du er enig i, at de passer på dig eller ej.</p>',
                                  # HTML to be placed on top of form
                                  table_row_header_width_pct=40,
                                  # width of row header (first column) in percent. default: 25
                                  table_rows_randomize=False,  # randomize order of displayed rows
                                  ),
        ]
    },
    'SQ3': {
        'page_title': '3. SANDSYNLIGHEDEN FOR, AT UDFØRE DIVERSE HANDLINGER',
        'survey_fields': [
            generate_likert_table(
                labels=['højst usandsynligt', 'usandsynligt', 'ikke sikkert', 'sandsynligt', 'højst sandsynligt'],
                choices_values=['highly unlikely', 'unlikely', 'not certain', 'likely', 'highly likely'],
                questions=[
                    ('s31_diff_taste', '… indrømme, at du har en anderledes smag end dine venner?'),
                    ('s32_camping', '… campere ude i vildmarken?'),
                    ('s33_beghorseracing', '… satse en dagløn på hestevæddeløb?'),
                    ('s34_investfund', '… investere 10% af din årsløn i en pensionsfond?'),
                    ('s35_drinking', '… drikke store mængder alkohol ved et socialt arrangement?'),
                    ('s36_taxdeduction', '… angive et lidt for højt fradrag til SKAT?'),
                    ('s37_disagreeauth',
                     '… erklære dig uenig med en autoritet, hvad angår et vigtigt emne?'),
                    ('s38_stakepokergame', '… satse en dagløn på et pokerspil med høje indsatser?'),
                    ('s39_affair', '… have en affære med en gift person?'),
                    ('s310_takecredit', '… tage æren for en anden persons arbejde?'),
                    ('s311_rundownski',
                     '… køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?'),
                    ('s312_invest5perincome',
                     '… investere 5% af din årsindtægt i en stærkt spekulativ aktie?'),
                    ('s313_whitewaterrafting',
                     '… tage på white water rafting om foråret når strømmen er stærkest?'),
                    ('s314_wageonmatch',
                     '… satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)?'),
                    ('s315_unsupportedsex', '… dyrke ubeskyttet sex?'),
                    ('s316_revealsecret', '… røbe en vens hemmelighed til en anden person?'),
                    ('s317_drivecarnobelt', '… køre i bil uden sele?'),
                    ('s318_investstartup',
                     '… investere 10% af din årsindtægt i en nystartet virksomhed?'),
                    ('s319_learnparachute', '… lære at springe i faldskærm?'),
                    ('s320_ridemoto', '… køre på motorcykel uden hjelm?'),
                    ('s321_choosecareer',
                     '… vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?'),
                    ('s322_sayunpopularcase',
                     '… sige hvad du mener om en upopulær sag til et møde på arbejdet?'),
                    ('s323_sunbathe', '… tage solbad uden solcreme?'),
                    ('s324_jumpbungee', '… springe bungy-jump fra en høj bro?'),
                    ('s325_takesmallplane', '… flyve en lille flyvemaskine?'),
                    ('s326_gohomealone',
                     '… gå alene hjem om natten gennem et af byens farlige kvarterer?'),
                    ('s327_movetofarawaycity', '… flytte til en by langt væk fra din familie?'),
                    ('s328_startnewcareer', "… påbegynde en ny karriere midt i 30'erne?"),
                    ('s329_leavekidathome',
                     '… efterlade dine små børn alene hjemme, imens du løber et ærinde?'),
                    ('s330_keeppurse',
                     '… beholde en pung du har fundet, som indeholder 1.000 kroner?'),
                    ('s331_movehouse', '… flytte til et hus, som ligger langs bredden af en flod:'),
                    ('s332_sendkidtoschool',
                     '… sende børn i skolen, imens DMI varsler om farligt vejr i dit område:'),
                    ('s333_drivefloodedroad', '… køre på en oversvømmet vej.'),
                    ('s334_parkcar',
                     '… parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.'),
                    ('s335_hiking',
                     '… tage på vandreture, imens DMI varsler om farligt vejr i området.')
                ],
                form_help_initial='<p>Vi vil bede dig angive sandsynligheden for, at du ville udføre nedenstående handlinger, hvis du befandt dig i de givne situationer. Hvor sandsynligt ville det være (hvis du befandt dig i den givne situation), at du ville...</p>',
                # HTML to be placed on top of form
                table_row_header_width_pct=40,
                # width of row header (first column) in percent. default: 25
                table_rows_randomize=False,  # randomize order of displayed rows
            ),
        ]
    },
    'SQ4': {
        'page_title': '4. RISIKO OPFATTELSE FORBUNDET MED DIVERSE HANDLINGER',
        'survey_fields': [
            generate_likert_table(labels=['Slet ikke risikofyldt', 'Meget lidt risiko', 'Nogen risiko', 'Høj risiko',
                                          'Allerhøjest risiko'],
                                  choices_values=['Not risky at all', 'Very little risk', 'No risk', 'High risk',
                                                  'Very high risk'],
                                  questions=[
                                      ('s41_diff_taste', '… indrømme, at du har en anderledes smag end dine venner?'),
                                      ('s42_camping', '… campere ude i vildmarken?'),
                                      ('s43_beghorseracing', '… satse en dagløn på hestevæddeløb?'),
                                      ('s44_investfund', '… investere 10% af din årsløn i en pensionsfond?'),
                                      ('s45_drinking', '… drikke store mængder alkohol ved et socialt arrangement?'),
                                      ('s46_taxdeduction', '… angive et lidt for højt fradrag til SKAT?'),
                                      ('s47_disagreeauth',
                                       '… erklære dig uenig med en autoritet hvad angår et vigtigt emne?'),
                                      ('s48_stakepokergame', '… satse en dagløn på et pokerspil med høje indsatser?'),
                                      ('s49_affair', '… have en affære med en gift person?'),
                                      ('s410_takecredit', '… tage æren for en anden persons arbejde?'),
                                      ('s411_rundownski',
                                       '… køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?'),
                                      ('s412_invest5perincome',
                                       '… investere 5% af din årsindtægt i en stærkt spekulativ aktie?'),
                                      ('s413_whitewaterrafting',
                                       '… tage på white water rafting om foråret når strømmen er stærkest?'),
                                      ('s414_wageonmatch',
                                       '… satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)??'),
                                      ('s415_unsupportedsex', '… dyrke ubeskyttet sex?'),
                                      ('s416_revealsecret', '… røbe en vens hemmelighed til en anden person?'),
                                      ('s417_drivecarnobelt', '… køre i bil uden sele?'),
                                      ('s418_investstartup',
                                       '… investere 10% af din årsindtægt i en nystartet virksomhed?'),
                                      ('s419_learnparachute', '… lære at springe i faldskærm?'),
                                      ('s420_ridemoto', '… køre på motorcykel uden hjelm?'),
                                      ('s421_choosecareer',
                                       '… vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?'),
                                      ('s422_sayunpopularcase',
                                       '… sige hvad du mener om en upopulær sag til et møde på arbejdet?'),
                                      ('s423_sunbathe', '… tage solbad uden solcreme?'),
                                      ('s424_jumpbungee', '… springe bungy-jump fra en høj bro?'),
                                      ('s425_takesmallplane', '… flyve en lille flyvemaskine?'),
                                      ('s426_gohomealone',
                                       '… gå alene hjem om natten gennem et af byens farlige kvarterer?'),
                                      ('s427_movetofarawaycity', '… flytte til en by langt væk fra din familie?'),
                                      ('s428_startnewcareer', "… påbegynde en ny karriere midt i 30'erne?"),
                                      ('s429_leavekidathome',
                                       '… efterlade dine små børn alene hjemme, imens du løber et ærinde?'),
                                      ('s430_keeppurse',
                                       '… beholde en pung du har fundet, som indeholder 1.000 kroner?'),
                                      ('s431_movehouse', '… flytte til et hus beliggende langs bredden af en flod:'),
                                      ('s432_sendkidtoschool',
                                       '… sende børn i skolen, imens DMI varsler om farligt vejr i dit område:'),
                                      ('s433_drivefloodedroad', '… køre på en oversvømmet vej.'),
                                      ('s434_parkcar',
                                       '… parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.'),
                                      ('s435_hiking',
                                       '… tage på vandreture, imens DMI varsler om farligt vejr i området.')
                                  ],
                                  form_help_initial='<p>Hvor risikofyldt synes du selv det er at...</p>',
                                  # HTML to be placed on top of form
                                  table_row_header_width_pct=40,
                                  # width of row header (first column) in percent. default: 25
                                  table_rows_randomize=False,  # randomize order of displayed rows
                                  ),
        ]
    },
    'SQ5': {
        'page_title': '5. DINE PRÆFERENCER',
        'survey_fields': [
            ('s51_prefered_option', {
                'text': 'Hvilken mulighed ville du foretrække?',
                'field': models.CharField(
                    choices=[['flatorcrown',
                              'Slå plat eller krone og vind 10.000 DKK med 50 procents sandsynlighed og 50 procents sandsynlighed for ingenting '],
                             ['win5kddk', 'Vind 5.000 DKK med sikkerhed'],
                             ['nomatter', 'Ligegyldigt, jeg synes begge muligheder er lige gode']
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s52_program_ab', {
                'text': '<p>Forestil dig, at regeringen forbereder sig på en mulig klimakatastrofe, hvor 600 mennesker forventes at omkomme. Regeringen kommer med to scenarier til at mindske katastrofen. Antag, at de videnskabelige estimater af konsekvenserne er nøjagtige.</p><p>Hvilke af de to forslag vil du foretrække?</p>',
                'field': models.CharField(
                    choices=[['progA',
                              'Scenarie A: 200 mennesker bliver reddet med sikkerhed, de resterende 400 er for usikkert til at kunne komme med et estimat.'],
                             ['progB',
                              'Scenarie B: Der er en tredjedel (33,3%) sandsynlighed for, at 600 mennesker bliver reddet, og to tredjedels (66,6%) sandsynlighed for, at ingen mennesker bliver reddet.']
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
            ('s53_program_cd', {
                'text': 'Regeringen fremsætter to yderligere scenarier, hvilket vil du foretrække?',
                'field': models.CharField(
                    choices=[['progC',
                              'Scenarie C: 400 mennesker vil omkomme med sikkerhed, de resterende 200 er for usikkert til at kunne komme med et estimat.'],
                             ['progD',
                              'Scenarie D: Der er en tredjedel (33,3%) sandsynlighed for, at ingen mennesker vil omkomme og to tredjedele (66,6%) sandsynlighed for, at 600 mennesker vil omkomme.']
                             ],
                    widget=widgets.RadioSelect()
                )
            }),
        ]
    },
    'SQ6': {
        'page_title': '6. PROBLEMHÅNDTERING',
        'survey_fields': [
            generate_likert_table(labels=['meget enig', 'enig', 'hverken enig eller uenig', 'uenig', 'meget uenig'],
                                  choices_values=['strongly agree', 'agree', 'neutral', 'disagree',
                                                  'strongly disagree'],
                                  questions=[
                                      ('s61_findsolution',
                                       'Jeg er god til at finde løsninger på forskellige udfordringer og problemer, som opstår i min hverdag.'),
                                      ('s62_findvalue',
                                       'Jeg oplever, at udfordringer og problemhåndtering skaber værdi for mit liv.'),
                                      ('s63_understand_issue',
                                       'Jeg er god til at forudse forskellige udfordringer og problemer i mit liv, og forstå deres betydning for mit liv.')
                                  ],
                                  form_help_initial='<p>Angiv for hvert udsagn, hvorvidt du er enig i, at de passer på dig eller ej.</p>',
                                  # HTML to be placed on top of form
                                  table_row_header_width_pct=40,
                                  # width of row header (first column) in percent. default: 25
                                  table_rows_randomize=False,  # randomize order of displayed rows
                                  ),
        ]
    },
    'SQ7': {
        'page_title': '7. PROBLEMHÅNDTERING I FÆLLESSKAB',
        'survey_fields': [
            generate_likert_table(labels=['meget enig', 'enig', 'hverken enig eller uenig', 'uenig', 'meget uenig'],
                                  choices_values=['strongly agree', 'agree', 'neutral', 'disagree',
                                                  'strongly disagree'],
                                  questions=[
                                      ('s71_adversity',
                                       'De vil med stor sandsynlighed overvinde mange af de udfordringer, der opstår i kølvandet på oversvømmelsen.'),
                                      ('s72_staycalm', 'De vil stille og roligt vurdere, hvad de skal gøre.'),
                                      ('s73_meaning_exp', 'De vil finde en mening med denne oplevelse.')
                                  ],
                                  form_help_initial='<p>Forestil dig at det område du bor i, bliver oversvømmet. Angiv, for hvert udsagn, hvorvidt du er enig i, at de passer til de mennesker der bor i nærområdet.</p>',
                                  # HTML to be placed on top of form
                                  table_row_header_width_pct=40,
                                  # width of row header (first column) in percent. default: 25
                                  table_rows_randomize=False,  # randomize order of displayed rows
                                  ),
        ]
    },
    'Email': {
        'page_title': 'Tak for din deltagelse',
        'survey_fields': [
            ('email', {
                'text': '<p>Vi trækker lod om 5 x gavekort på 200,- til gavmildt.dk blandt alle gennemførte besvarelser.</p> <p>Hvis du vil være med i lodtrækning skal vi brug din e-mail adresse.</p><p>Dette er kun for at kunne kontakte dig i tilfælde af, at du vinder.    Din e-mail skal ikke opbevares i databasen.</p> <p>E-mail:</p>',
                'field': models.CharField(blank=True, default='')
            }),
        ]
    },
}

Player = create_player_model_for_survey('survey3rd.models',
                                        SURVEY_DEFINITIONS)
