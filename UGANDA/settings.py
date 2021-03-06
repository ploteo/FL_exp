from os import environ


# semi randomize sequence in Block 1

import random

if random.randint(0, 1) == 1:
    sequence = ['FL_welcome', 'FL_DG', 'FL_TG',
                'FL_time', 'FL_risk', 'FL_payments']
else:
    sequence = ['FL_welcome', 'FL_TG', 'FL_DG',
                'FL_time', 'FL_risk', 'FL_payments']
print(sequence)


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

LANGUAGE_CODE = 'en' # <- Chewa (also known as Nyanja) UGANDA

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 0.00,
    'doc': ""
}
# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'sente ezza wano'#CHANGE HERE
USE_POINTS = True
POINTS_CUSTOM_NAME = 'obugoba'#CHANGE HERE

SESSION_CONFIGS = [

 dict(
     name='FL_block_1', 
     display_name='FL_block1',
     num_demo_participants=4,
     participation_fee=int(4),
     real_world_currency_per_point=0.01,
     block = "block1",#to control the display of results
    app_sequence=sequence
 ),
    dict(
     name='FL_block_2',
     display_name='FL_block2',
     num_demo_participants=8,
     participation_fee=int(4),
     real_world_currency_per_point=0.01,
     block = "block2",  # to control the display of results
     app_sequence=['FL_welcome', 'FL_PGG',
                   'FL_time', 'FL_risk', 'FL_payments']
  ),
#     dict(
#      name='FL_PGG',
#      display_name='FL_PGG',
#      num_demo_participants=4,
#      participation_fee=4,
#      real_world_currency_per_point=0.01,
#      treatment="identity",
#      app_sequence=['FL_PGG']
#  ),
#     dict(
#         name='FL_TG',
#         display_name='FL_TG',
#         num_demo_participants=2,
#         participation_fee = 4,
#         real_world_currency_per_point= 0.01,
#         app_sequence=['FL_TG']
#         ),
#     dict(
#     name='FL_DG',
#     display_name='FL_DG',
#     num_demo_participants=2,
#     participation_fee=4,
#     real_world_currency_per_point=0.01,
#     app_sequence=['FL_DG']
# ),
#     dict(
#         name='FL_time',
#         display_name="FL_time",
#         num_demo_participants=1,
#         app_sequence=['FL_time']
# ),
#     dict(
#         name='FL_risk',
#         display_name="FL_risk",
#         num_demo_participants=1,
#         app_sequence=['FL_risk']
# ),
#     dict(
#         name='FL_welcome',
#         display_name="FL_welcome",
#         num_demo_participants=1,
#      participation_fee=4,
#      real_world_currency_per_point=0.01,
#         app_sequence=['FL_welcome']
#  )
]


ROOMS = [
    dict(name='live_demo_1', display_name='Room for live 1 (no participant labels)'),
	 dict(name='live_demo_2', display_name='Room for live 2 (no participant labels)'),
 dict(
        name='econ_lab',
        display_name='Experimental Economics Lab 40s',
        participant_label_file='_rooms/labels.txt',
	use_secure_urls=True
    )]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = ''

INSTALLED_APPS = ['otree','otreeutils']
