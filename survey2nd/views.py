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
        's33_understand_issue',
        's41_adversity',
        's42_staycalm',
        's43_meaning_exp',
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
        's61_movehouse',
        's62_sendkidtoschool',
        's63_drivefloodedroad',
        's64_parkcar',
        's65_hiking',
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

    def vars_for_template(self):
        return dict(total_payoff=self.participant.payoff,
                    )

page_sequence = [SurveyQuestions]
