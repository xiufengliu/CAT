from __future__ import division


from . import models
from ._builtin import Page


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
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

class SQ3(Page):
    form_model = models.Player
    form_fields = [
        's31_findsolution',
        's32_findvalue',
        's33_understand_issue'
    ]

class SQ4(Page):
    form_model = models.Player
    form_fields = [
        's41_adversity',
        's42_staycalm',
        's43_meaning_exp'
    ]

class SQ5(Page):
    form_model = models.Player
    form_fields = [
        's51_diff_taste',
        's52_camping',
        's53_beghorseracing',
        's54_investfund',
        's55_drinking',
        's56_taxdeduction',
        's57_disagreeauth',
        's58_stakepokergame',
        's59_affair',
        's510_takecredit',
        's511_rundownski',
        's512_invest5perincome',
        's513_whitewaterrafting',
        's514_wageonmatch',
        's515_unsupportedsex',
        's516_revealsecret',
        's517_drivecarnobelt',
        's518_investstartup',
        's519_learnparachute',
        's520_ridemoto',
        's521_choosecareer',
        's522_sayunpopularcase',
        's523_sunbathe',
        's524_jumpbungee',
        's525_takesmallplane',
        's526_gohomealone',
        's527_movetofarawaycity',
        's528_startnewcareer',
        's529_leavekidathome',
        's530_keeppurse',
        's531_movehouse',
        's532_sendkidtoschool',
        's533_drivefloodedroad',
        's534_parkcar',
        's535_hiking'
    ]

class SQ6(Page):
    form_model = models.Player
    form_fields = [
        's61_diff_taste',
        's62_camping',
        's63_beghorseracing',
        's64_investfund',
        's65_drinking',
        's66_taxdeduction',
        's67_disagreeauth',
        's68_stakepokergame',
        's69_affair',
        's610_takecredit',
        's611_rundownski',
        's612_invest5perincome',
        's613_whitewaterrafting',
        's614_wageonmatch',
        's615_unsupportedsex',
        's616_revealsecret',
        's617_drivecarnobelt',
        's618_investstartup',
        's619_learnparachute',
        's620_ridemoto',
        's621_choosecareer',
        's622_sayunpopularcase',
        's623_sunbathe',
        's624_jumpbungee',
        's625_takesmallplane',
        's626_gohomealone',
        's627_movetofarawaycity',
        's628_startnewcareer',
        's629_leavekidathome',
        's630_keeppurse',
        's631_movehouse',
        's632_sendkidtoschool',
        's633_drivefloodedroad',
        's634_parkcar',
        's635_hiking'
    ]

class SQ7(Page):
    form_model = models.Player
    form_fields = [
        's71_lookpainting',
        's72_thingsinplace',
        's73_remainunkind',
        's74_nobodylikeme',
        's75_afraidfeelingpain',
        's76_hardtolie',
        's77_sciboring',
        's78_postponetask',
        's79_criticism',
        's710_gettouchstranger',
        's711_worry',
        's712_wondering',
        's713_goodimg',
        's714_precise',
        's715_agreeothers',
        's716_talkothers',
        's717_overcome',
        's718_famous',
        's719_lovepeople',
        's720_dothings',
        's721_staycalm',
        's722_wellmanner',
        's723_tear',
        's724_soap'
    ]


page_sequence = [SQ1, SQ2, SQ3, SQ4, SQ5, SQ6, SQ7]
