from __future__ import division
from . import models
from ._builtin import Page
from otreeutils.surveys import SurveyPage, setup_survey_pages

'''
class Intro(Page):
    pass

class SQ1(SurveyPage):
    pass

class SQ2(SurveyPage):
    pass
'''

class SQ3(SurveyPage):
    pass

class SQ4(SurveyPage):
    pass

class SQ5(SurveyPage):
    pass

class SQ6(SurveyPage):
    pass

class SQ7(SurveyPage):
    pass

class Email(SurveyPage):
    pass

class Thanks(Page):
    pass

survey_pages = [SQ3, SQ4, SQ5, SQ6, SQ7, Email]

# Common setup for all pages (will set the questions per page)
setup_survey_pages(models.Player, survey_pages)

page_sequence = [SQ3, SQ4, SQ5, SQ6, SQ7, Email, Thanks]

# add the survey pages to the page sequence list
#page_sequence.extend(survey_pages)
#page_sequence.append(Thanks)


