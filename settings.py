from os import environ


SESSION_CONFIGS = [
    dict(
        name = "CAT_Apps",
        display_name = "CAT Apps",
        real_world_currency_per_point = 0.0125,
        num_demo_participants= 3,
        app_sequence= [
            'welcome',  # Welcome
            'control',  # Phase 1
            # 'control_forcedloss',  # Phase 1
            'ambiguity',  # Phase 2
            'loss',  # Phase 3
            'myopia',  # Phase 4
            'coordination',  # Phase 5
            'coordination_amb',  # Phase 6
            'communication',  # Phase 7
            'payment_info',  # Payment summary
            'survey1st'  # survey quesitons
        ],
    ),
 dict(
        name = "CATC_Apps",
        display_name = "CAT+C Apps",
        real_world_currency_per_point = 0.0125,
        num_demo_participants = 3,
        app_sequence = [
            'welcome',  # Welcome
            'control_forcedloss',  # Phase 1
            'ambiguity',  # Phase 2
            'coordination',  # Phase 5
            'coordination_amb',  # Phase 6
            'communication',  # Phase 7
            'myopia',
            'payment_info',  # Payment summary
            'survey1st'  # survey quesitons
        ],
),
dict(
        name = "CATD_Apps",
        display_name = "CAT+D Apps",
        real_world_currency_per_point = 0.0125,
        num_demo_participants = 3,
        app_sequence = [
            'welcome',  # Welcome
            'control',  # Phase 1
            'ambiguity',  # Phase 2
            'coordination',  # Phase 5
            'coordination_amb',  # Phase 6
            'communication',  # Phase 7
            'payment_info',  # Payment summary
            'survey1st'  # survey quesitons
        ],
),
dict(
        name = "CATE_Apps",
        display_name = "CAT+E Apps",
        real_world_currency_per_point = 0.0125,
        num_demo_participants = 1,
        app_sequence = [
            'survey2nd'  # survey quesitons
        ],
)
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'DKK'
USE_POINTS = True

ROOMS = [
    dict(
        name='CAT_Room',
        display_name='CAT Room',
        participant_label_file='_rooms/cat.txt',
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '#8_on^o3&#i+ajkyobxsv^)a)l896or+o=n)=_5&x!+u&9s^1='

INSTALLED_APPS = ['otree']
