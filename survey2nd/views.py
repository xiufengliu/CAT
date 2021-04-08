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

class SQ5(Page):
    form_model = models.Player
    form_fields = [
        's51_prefered_option',
        's52_program_ab',
        's53_program_cd'
        ]

class SQ6(Page):
    form_model = models.Player
    form_fields = [
        's61_findsolution',
        's62_findvalue',
        's63_understand_issue'
    ]

class SQ7(Page):
    form_model = models.Player
    form_fields = [
        's71_adversity',
        's72_staycalm',
        's73_meaning_exp'
    ]

class SQ3(Page):
    form_model = models.Player
    form_fields = [
        's31_diff_taste',
        's32_camping',
        's33_beghorseracing',
        's34_investfund',
        's35_drinking',
        's36_taxdeduction',
        's37_disagreeauth',
        's38_stakepokergame',
        's39_affair',
        's310_takecredit',
        's311_rundownski',
        's312_invest5perincome',
        's313_whitewaterrafting',
        's314_wageonmatch',
        's315_unsupportedsex',
        's316_revealsecret',
        's317_drivecarnobelt',
        's318_investstartup',
        's319_learnparachute',
        's320_ridemoto',
        's321_choosecareer',
        's322_sayunpopularcase',
        's323_sunbathe',
        's324_jumpbungee',
        's325_takesmallplane',
        's326_gohomealone',
        's327_movetofarawaycity',
        's328_startnewcareer',
        's329_leavekidathome',
        's330_keeppurse',
        's331_movehouse',
        's332_sendkidtoschool',
        's333_drivefloodedroad',
        's334_parkcar',
        's335_hiking'
    ]

class SQ4(Page):
    form_model = models.Player
    form_fields = [
        's41_diff_taste',
        's42_camping',
        's43_beghorseracing',
        's44_investfund',
        's45_drinking',
        's46_taxdeduction',
        's47_disagreeauth',
        's48_stakepokergame',
        's49_affair',
        's410_takecredit',
        's411_rundownski',
        's412_invest5perincome',
        's413_whitewaterrafting',
        's414_wageonmatch',
        's415_unsupportedsex',
        's416_revealsecret',
        's417_drivecarnobelt',
        's418_investstartup',
        's419_learnparachute',
        's420_ridemoto',
        's421_choosecareer',
        's422_sayunpopularcase',
        's423_sunbathe',
        's424_jumpbungee',
        's425_takesmallplane',
        's426_gohomealone',
        's427_movetofarawaycity',
        's428_startnewcareer',
        's429_leavekidathome',
        's430_keeppurse',
        's431_movehouse',
        's432_sendkidtoschool',
        's433_drivefloodedroad',
        's434_parkcar',
        's435_hiking'
    ]

class SQ2(Page):
    form_model = models.Player
    form_fields = [
        's21_lookpainting',
        's22_thingsinplace',
        's23_remainunkind',
        's24_nobodylikeme',
        's25_afraidfeelingpain',
        's26_hardtolie',
        's27_sciboring',
        's28_postponetask',
        's29_criticism',
        's210_gettouchstranger',
        's211_worry',
        's212_wondering',
        's213_goodimg',
        's214_precise',
        's215_agreeothers',
        's216_talkothers',
        's217_overcome',
        's218_famous',
        's219_lovepeople',
        's220_dothings',
        's221_staycalm',
        's222_wellmanner',
        's223_tear',
        's224_soap'
    ]

class Email(Page):
    form_model = models.Player
    form_fields = ['email',]

class Thanks(Page):
    pass


page_sequence = [Intro, SQ1, SQ2, SQ3, SQ4, SQ5, SQ6, SQ7, Email, Thanks]
