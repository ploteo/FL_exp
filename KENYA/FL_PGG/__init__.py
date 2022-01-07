from otree.api import *
from gettext import gettext
import random

doc = """
pgg_standard
- 2 rounds partner matching
- treatment identity randomized at the group level
"""


class Constants(BaseConstants):
    name_in_url = 'FL_PGG_standard'
    players_per_group = 4
    num_rounds = 2
    endowment_high = cu(200)
    endowment_low = cu(100)
    endowment_medium = cu(150)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contributions = models.CurrencyField()
    individual_share = models.CurrencyField()
    total_earnings = models.CurrencyField()
    
class Player(BasePlayer):
    identity_treatment = models.CharField() #NOTE: added this to randomize at the group level
    endowment = models.CurrencyField()
    contribution = models.CurrencyField(min=0, max=Constants.endowment_medium)
    #identity task
    I1 = models.IntegerField()
    I2 = models.IntegerField()
    I3 = models.IntegerField()
    I4 = models.IntegerField()

    # control questions
    Q1_1 = models.IntegerField()
    Q1_2 = models.IntegerField()

    # final questionnaire
#2 How much do you trust that the people in your group put money in the common account?
    Q2_2 = models.IntegerField(
        choices=[
            [1, gettext("Not at all")],
            [2, gettext("Little")],
            [3, gettext("Average")],
            [4, gettext("Fairly ")],
            [5, gettext("Completely")],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    # 1.    How much do you think that you understood the instructions of the decisions you just made?
    # Code: 1 = Very little
    # 2 = Little
    # 3 = Average
    # 4 = Fairy well
    # 5 = Completely.
    Q2_1 = models.IntegerField(
        choices=[
            [1, gettext("Not at all")],
            [2, gettext("Little")],
            [3, gettext("Average")],
            [4, gettext("Fairly well")],
            [5, gettext("Very well")],
        ],
        widget=widgets.RadioSelectHorizontal,
    )


# FUNCTIONS
def I1_choices(player):
    if player.identity_treatment == "identity": #NOTE:changed here to randomize at group level
        if player.id_in_group==1:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'au ya joto.'],[3,'baridi']]
        if player.id_in_group==2:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'uwazi.'],[3,'ya']]
        if player.id_in_group==3:
            choices = [[2,'kuwa'], [1,'Inaweza'], [4,'chumvi.'],[3,'na']]
        if player.id_in_group==4:
           choices = [[2,'fanya'], [1,'Ina'], [4,'iende.'],[3,'kiu']]
    else:
        if player.id_in_group==1:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'au ya joto.'],[3,'kuwa baridi']]
        if player.id_in_group==2:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'wazi.'],[3,'kuwa']]
        if player.id_in_group==3:
            choices = [[2,'inaweza'], [1,' Maji'], [4,'na chumvi.'],[3,'kuwa']]
        if player.id_in_group==4:
           choices = [[2,'hufanya'], [1,'Maji'], [4,'kuondoka.'],[3,'kiu']]
    return choices

def I2_choices(player):
    if player.identity_treatment == "identity": #NOTE:changed here to randomize at group level
        if player.id_in_group==1:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'au ya joto.'],[3,'baridi']]
        if player.id_in_group==2:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'uwazi.'],[3,'ya']]
        if player.id_in_group==3:
            choices = [[2,'kuwa'], [1,'Inaweza'], [4,'chumvi.'],[3,'na']]
        if player.id_in_group==4:
           choices = [[2,'fanya'], [1,'Ina'], [4,'iende.'],[3,'kiu']]
    else:
        if player.id_in_group==1:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'au ya joto.'],[3,'kuwa baridi']]
        if player.id_in_group==2:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'wazi.'],[3,'kuwa']]
        if player.id_in_group==3:
            choices = [[2,'inaweza'], [1,' Maji'], [4,'na chumvi.'],[3,'kuwa']]
        if player.id_in_group==4:
           choices = [[2,'hufanya'], [1,'Maji'], [4,'kuondoka.'],[3,'kiu']]
    return choices

def I3_choices(player):
    if player.identity_treatment == "identity": #NOTE:changed here to randomize at group level
        if player.id_in_group==1:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'au ya joto.'],[3,'baridi']]
        if player.id_in_group==2:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'uwazi.'],[3,'ya']]
        if player.id_in_group==3:
            choices = [[2,'kuwa'], [1,'Inaweza'], [4,'chumvi.'],[3,'na']]
        if player.id_in_group==4:
           choices = [[2,'fanya'], [1,'Ina'], [4,'iende.'],[3,'kiu']]
    else:
        if player.id_in_group==1:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'au ya joto.'],[3,'kuwa baridi']]
        if player.id_in_group==2:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'wazi.'],[3,'kuwa']]
        if player.id_in_group==3:
            choices = [[2,'inaweza'], [1,' Maji'], [4,'na chumvi.'],[3,'kuwa']]
        if player.id_in_group==4:
           choices = [[2,'hufanya'], [1,'Maji'], [4,'kuondoka.'],[3,'kiu']]
    return choices

def I4_choices(player):
    if player.identity_treatment == "identity": #NOTE:changed here to randomize at group level
        if player.id_in_group==1:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'au ya joto.'],[3,'baridi']]
        if player.id_in_group==2:
           choices = [[2,'kuwa'], [1,'Inaweza'], [4,'uwazi.'],[3,'ya']]
        if player.id_in_group==3:
            choices = [[2,'kuwa'], [1,'Inaweza'], [4,'chumvi.'],[3,'na']]
        if player.id_in_group==4:
           choices = [[2,'fanya'], [1,'Ina'], [4,'iende.'],[3,'kiu']]
    else:
        if player.id_in_group==1:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'au ya joto.'],[3,'kuwa baridi']]
        if player.id_in_group==2:
           choices = [[2,'inaweza'], [1,'Maji'], [4,'wazi.'],[3,'kuwa']]
        if player.id_in_group==3:
            choices = [[2,'inaweza'], [1,' Maji'], [4,'na chumvi.'],[3,'kuwa']]
        if player.id_in_group==4:
           choices = [[2,'hufanya'], [1,'Maji'], [4,'kuondoka.'],[3,'kiu']]
    return choices

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        subsession.group_randomly()
        for g in subsession.get_groups():
            for p in g.get_players():
                p.endowment = Constants.endowment_medium
    else:
        subsession.group_like_round(1)

        #-------------------------------
        ## original 
        #-------------------------------
        for g in subsession.get_groups():
            if random.randint(0, 1) == 1:#NOTE: added this to randomize at group level
                treatment = 'no_identity'
            else:
                treatment = 'identity'
            print(treatment)
        #-------------------------------
        ## use group id for the randomization
        #-------------------------------
        # for g in subsession.get_groups():
        #     if g.id_in_subsession % 2 == 0:
        #         treatment = 'no_identity'
        #     else:
        #         treatment = 'identity'
        #     print(treatment)            
        #-------------------------------
        
            for p in g.get_players():
                p.identity_treatment = treatment #NOTE: added this to randomize at group level
                p.endowment = Constants.endowment_medium
        # to play outside blocks
                try:
                    if p.session.config['block'] == "block1":
                        continue
                except:
                    p.participant.vars['game_count'] = 0
def set_payoffs(group: Group):
    players = group.get_players()
    choices = [p.contribution for p in players]
    group.total_contributions = sum(choices)
    group.individual_share = (
        group.total_contributions * Constants.multiplier
    ) / Constants.players_per_group
    for p in players:
        p.payoff = p.endowment - p.contribution + group.individual_share
        payoff_hist = []
        contrib_hist = []
        total_contrib_hist = []
        endowment_hist = []
        # needed to store the data
        for i in p.in_all_rounds():
            payoff_hist.append(i.payoff)
            contrib_hist.append(i.contribution)
            total_contrib_hist.append(i.group.total_contributions)
            endowment_hist.append(i.endowment)
        # for later when we pay everything at the end
        p.participant.vars['PGG_info'] = [endowment_hist, contrib_hist, total_contrib_hist, payoff_hist]
        print(p.participant.vars['PGG_info'])


def update_counter(group: Group):
    for p in group.get_players():
        p.participant.vars['game_count'] += 1


# PAGES

class ChoiceWaitPageInit(WaitPage):
    # update counter
    after_all_players_arrive = 'update_counter'
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Header(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    def vars_for_template(player: Player):
        return {
            'counter': player.participant.vars['game_count']
        }

class Instructions_container(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_common': Constants.players_per_group * Constants.endowment_medium,
            'total_surplus': Constants.players_per_group * Constants.endowment_medium * 2,
            'individual_share': Constants.endowment_medium * 2,
            'counter': player.participant.vars['game_count']
        }

class Instructions_container_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_common': Constants.players_per_group * Constants.endowment_medium,
            'total_surplus': Constants.players_per_group * Constants.endowment_medium * 2,
            'individual_share': Constants.endowment_medium * 2,
            'count':1,
            'treatment': player.identity_treatment #NOTE:changed here to randomize at group level
        }

class Examples(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_common': Constants.players_per_group * Constants.endowment_medium,
            'total_surplus': Constants.players_per_group * Constants.endowment_medium * 2,
            'individual_share': Constants.endowment_medium * 2,
        }

class Instructions(Page):
    def vars_for_template(player: Player):
        return {
            'total_common': Constants.players_per_group * Constants.endowment_medium,
            'total_surplus': Constants.players_per_group * Constants.endowment_medium * 2,
            'individual_share': Constants.endowment_medium * 2,
        }

class Instructions2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2


class Questionnaire1(Page):
    form_model = 'player'
    form_fields = ['Q1_1', 'Q1_2']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def error_message(player: Player, values):
        if values["Q1_1"] != 350:
            return gettext('Please check your answer to question 1')
        if  values["Q1_2"] != 300:
            return gettext('Please check your answer to question 2')

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_common': Constants.players_per_group * Constants.endowment_medium,
            'total_surplus': Constants.players_per_group * Constants.endowment_medium * 2,
            'individual_share': Constants.endowment_medium * 2,
        }



class Pregame(Page):
    @staticmethod
    def player(self):
        return self.round_number == 1


class Instructions2(Page):
    def is_displayed(self):
        return self.round_number == 2


class Identity_task(Page):
    def is_displayed(self):
        return self.round_number == 2

    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from constants and store them in a dictionary
        return {
            'treatment': player.identity_treatment, #NOTE:changed here to randomize at group level
            'id': player.id_in_group
        }

class Identity_task_ALT(Page):

    form_model = 'player'
    form_fields = ['I1','I2','I3','I4']

    @staticmethod
    def error_message(player, values):
        if values["I1"] != int(1) :
            return gettext('The sequence is not correct, please Retry')
        if values["I2"] != int(2) :
            return gettext('The sequence is not correct, please Retry')   
        if values["I3"] != int(3) :
            return gettext('The sequence is not correct, please Retry')  
        if values["I4"] != int(4) :
            return gettext('The sequence is not correct, please Retry')               

    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(player: Player):
        # retrieve values from constants and store them in a dictionary
        return {
            'treatment': player.identity_treatment,#NOTE:changed here to randomize at group level
            'id': player.id_in_group
        }        


class Identity_task_feedback(Page):
    def is_displayed(self):
        return self.round_number == 2

    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from constants and store them in a dictionary
        return {
            'treatment': player.identity_treatment,#NOTE:changed here to randomize at group level
            'id': player.id_in_group
        }


class Choices(Page):
    form_model = 'player'
    form_fields = ['contribution']
    # values that are to be displayed (dictionary)
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from constants and store them in a dictionary
        return {'Round': player.subsession.round_number, 'Endowment': player.endowment}


class MyResultsWaitPage(WaitPage):
    # template_name = 'FL_pgg/MyResultsWaitPage.html'
    after_all_players_arrive = 'set_payoffs'


class MyWaitPage(WaitPage):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):  # display only if it is not in block
        try:
            return player.session.config['block'] != "block1" and player.session.config['block'] != "block2" 
        except:
            return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        # retrieve historical data
        hist = [
            [g.endowment for g in player.in_all_rounds()],
            [g.contribution for g in player.in_all_rounds()],
            [g.total_contributions for g in player.group.in_all_rounds()],
            [g.payoff for g in player.in_all_rounds()],
        ]
        # old values
        table_hist = []
        for j in range(0, player.round_number):
            print(j)
            t = []
            t.append(j + 1)
            for k in hist:
                t.append(k[j])
            table_hist.append(t)
        print(table_hist)
        return {'table_hist': table_hist}

        #STORE FOR LATER


    def is_displayed(player: Player):  # display only if it is not in block
        try:
            return player.session.config['block'] != "block1" and player.session.config['block'] != "block2"
        except:
            return True


class Questionnaire2(Page):
    form_model = 'player'
    form_fields = ['Q2_1','Q2_2']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2


# <!-- put here the questionnaire -->
page_sequence = [
    ChoiceWaitPageInit,
    Header,
    Instructions_container,
    Instructions_container_2,
    Examples,
    Questionnaire1,
    Identity_task_ALT,
    MyWaitPage,
    Identity_task_feedback,
    Choices,
    MyResultsWaitPage,
    Results,
    Questionnaire2
]
