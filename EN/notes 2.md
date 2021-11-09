**To be inputed before starting**

- Name and place of the organizations - > institutions.csv in FL_Welcome
- Choices of organizations in TG - > choices_inst.csv in FL_Welcome
- Conversion rate of tokens in Local Currency -> settings.py -> "real_world_currency_per_point=0.01"
    - \# Tokens * real_world_currency_per_point = LC
- Show up fee (ein LC) -> settings.py -> participation_fee=int(4)
- Number of participants -> settings.py

# Randomizations
- The randomization of block 1 is at the session level 
- The randomization of ientity in block 2 at the group level (to be developed @TODO:)
