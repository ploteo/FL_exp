from otree.api import *
import random
import csv

doc = """
Relevant parameters are imported here
"""
#-------------------------------------
# Import relevant parameters
#-------------------------------------
# Institutions
with open('FL_welcome/institutions.csv', encoding='utf-8') as file:
    read = list(csv.DictReader(file))
    print([read[0],read[1]])#for two organizations

# Import choices of the institution from an external file
    with open('FL_welcome/choices_inst.csv', encoding='utf-8') as file:
        choices_inst = list(csv.DictReader(file))
        print([choices_inst[0], choices_inst[1]])

# Parameters

#-------------------------------------


class Constants(BaseConstants):
    name_in_url = 'FL_welcome'
    players_per_group = None
    num_rounds = 1
    # here the names of the institution
    #institutions = [institutions[0]["Inst_name"],institutions[1]["Inst_name"]]

class Subsession(BaseSubsession):
    exch_rate = models.FloatField()
    show_up = models.FloatField()  # models.RealWorldCurrencyField()
    block=models.CharField()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
def creating_session(subsession: Subsession):
    subsession.exch_rate = subsession.session.config['real_world_currency_per_point']
    subsession.show_up = int(subsession.session.config['participation_fee'])
    try:
        subsession.block = player.session.config['block']
    except:
        subsession.block = "None"

    for g in subsession.get_groups():
        for p in g.get_players():
            p.participant.vars['game_count'] = 0  # to count the sequence games
            # to have the same random institution across rounds
            rand_inst = random.randint(0, 1)
            # to get random institution at the individual level
            p.participant.vars['institution'] = read[rand_inst]
            p.participant.vars['institution_choices'] = choices_inst[rand_inst]
            #retrieve the right choices set for that institution
            print(p.participant.vars['institution'])

# PAGES
class Welcome(Page):
    def vars_for_template(player: Player):
        try:
            if player.session.config['block'] == "block2":
                games = 3
            elif player.session.config['block'] == "block1":
                games = 4
        except:
            games= ""

        return{
        'exch_rate_disp': player.subsession.exch_rate*10,
        'show_up': player.subsession.show_up,
        'games' : games
        }


class Welcome2(Page):
    def vars_for_template(player: Player):
        try:
            if player.session.config['block'] == "block2":
                games = 3
            elif player.session.config['block'] == "block1":
                games = 4
        except:
            games = ""

        return{
            'exch_rate_disp': player.subsession.exch_rate*10,
            'show_up': player.subsession.show_up,
            'games': games
        }

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Welcome, Welcome2]
