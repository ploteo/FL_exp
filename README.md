# Versions

- The reference app is in folder "EN" (english version)
- The other folders contain translations of the reference app.

# Our apps

Two main experiments are developed, *block 1 and block 2*, that differ in the sequence of apps that are presented to participants


## Block 1
The following apps are contained in Block 1

1) *FL_welcome* 
    - This app must be the first in te sequence. It displays a welcoem messag eand general instructions.
    - It also loads pieces iof information about organizations from external .csv files. 

        **choices_inst.csv**

        Example: 

        | Institution | Choice_other_0 | Choice_other_30 | Choice_other_60 | Choice_other_90 |
        |-------------|----------------|-----------------|-----------------|-----------------|
        | A           | 0              | 15              | 80              | 120             |
        | B           | 0              | 20              | 40              | 100             |

                
                
                
        **institutions.csv**
        Example: 

        | Inst_Name | Inst_Type | Inst_Area | Inst_Product  |
        |-------------|----------------|-----------------|-----------------|-----------------|
        | A           | NGO              |Place X              | new nutrient-dense food product                  |
        | B           | Association              | Place Y              | new water irrigation saving technology           |

        - &#9888;  These files must be filled with the correct information about local organizations  and preserving the original structure
  
- *FL_DG* 
  - A Dictator Game: 2 phases, first with a peer then with the organization
    - Both choose as Dictators and know aftewards their actual role
- *FL_TG* 
  - A mini-investment game: 2 phases, first with a peer then with the organization
    - Play either as Recipient or as Sender
      - Both receive th eendowment
      - Strategy method  
- *FL_time*
  - A MPL estimation of time preferences
- *FL_risk*
  - A MPL estimation of risk preferences
6) *FL_payments*
   - Displays all payments and feedbacks


The order of FL_DG, FL_TG, FL_time, FL_risk can be randomized in *settings.py* (see below)

## Block 2

The following apps are contained in Block 2

1) *FL_welcome* 
    - This app must be the first in te sequence. It displays a welcome message and general instructions.

-FL_PGG
    - A 4-player PGG over 2 rounds in a partner fashion
      - Round 1: PGG
      - Task: subjects are either assigned to an *identity task* (to create group identity) or to an *individual task*
        - Controlled from *settings.py* (see below)
      - Round 2: PGG

- *FL_time*
  - A MPL estimation of time preferences
- *FL_risk*
  - A MPL estimation of risk preferences

6) *FL_payments*
   - Displays all payments and feedbacks

# settings.py

This file controls general settings of the experiment. It looks like this


```python

LANGUAGE_CODE = 'en' # <- CHANGE GERE: it,en

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 0.00,
    'doc': ""
}
# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'LC'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'Tokens'

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
    num_demo_participants=4,
    participation_fee=int(4),
    real_world_currency_per_point=0.01,
    block = "block2",  # to control the display of results
    treatment ="identity", #identity to have identity in the task of PGG
    app_sequence=['FL_welcome', 'FL_PGG','FL_time', 'FL_risk', 'FL_payments']
 )
]
[...]
```

The following key variables can be controlled from here

- General
    - **LANGUAGE_CODE** = 'en'
      - The language used for system feedbacks
   - **REAL_WORLD_CURRENCY_CODE** = 'LC'
     - Name of the local currency
   - **USE_POINTS** = True
     - Is the game played with points (True)
   - **POINTS_CUSTOM_NAME** = 'Tokens'
     - Name of Tokens (to be translated)

- Block specific
   - **participation_fee**
     - Payment for participation in LC
   - **block**
     - either *block1* or *block2*, accordingly   
   - **real_world_currency_per_point**
     - Conversion rate of Tokens into real currency
   - **app_sequence**
     - The sequence of apps in a list
       - Can be randomized or decided ex-ante 
         - &#9888; FL_welcome and FL_oayment must always be first and last
   - **treatment** (block2 only)
     - = identity -> participants go through a group identity task (word game)
     - = individual -> participants go through an individual task (word game)

This is an example of how to randomize the sequence of apps at the session level

```python
from os import environ

#this is for block 1
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
```