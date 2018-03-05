import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') in {None, '', '0'}:
    DEBUG = True
else:
    DEBUG = False


# don't share this with anybody.
SECRET_KEY = 'gf=*)8aol&8+0v2fj7ozqa=-b9um5p3es^5d2b71w7kyqb(k-0'


DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        default='postgres://xiuli:Abcd1234@localhost:5432/otree'
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        #default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = 'DEMO' #environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'admin1234' #environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'DKK'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'tokens'


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otreechat']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'cat',
        'display_name': 'Room for 27 persons maximum',
        'participant_label_file': '_rooms/cat.txt',
    },
]


mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': "CAT_Apps",
        'display_name': "CAT Apps",
        "real_world_currency_per_point": 0.0125,
        'num_demo_participants': 3,
        'app_sequence': [
                        'welcome',              # Welcome
                        'control',              # Phase 1
                        #'control_forcedloss',  # Phase 1
                        'ambiguity',            # Phase 2
                        'loss',                 # Phase 3
                        'myopia',               # Phase 4
                        'coordination',         # Phase 5
                        'coordination_amb',     # Phase 6
                        'communication',        # Phase 7
                        'payment_info',         # Payment summary
                        'survey_questions'      # survey quesitons
                         ],
    }
,
    {
        'name': "CATC_Apps",
        'display_name': "CAT+C Apps",
        "real_world_currency_per_point": 0.0125,
        'num_demo_participants': 3,
        'app_sequence': [
            'welcome',  # Welcome
            'control_forcedloss',  # Phase 1
            'ambiguity',  # Phase 2
            'coordination',  # Phase 5
            'coordination_amb',  # Phase 6
            'communication',  # Phase 7
            'myopia',
            'payment_info',  # Payment summary
            'survey_questions'  # survey quesitons
        ],
    }
,
    {
        'name': "CATD_Apps",
        'display_name': "CAT+D Apps",
        "real_world_currency_per_point": 0.0125,
        'num_demo_participants': 3,
        'app_sequence': [
            'welcome',  # Welcome
            'control',  # Phase 1
            'ambiguity',  # Phase 2
            'coordination',  # Phase 5
            'coordination_amb',  # Phase 6
            'communication',  # Phase 7
            'payment_info',  # Payment summary
            'survey_questions'  # survey quesitons
        ],
    }

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
