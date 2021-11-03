import random
from gettext import gettext
from otree.api import *


author = 'M. Ploner'
doc = """
    MPL time preferences
"""


class Constants(BaseConstants):
    name_in_url = 'MPL_time'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    A = 100
    B = [105, 111, 118, 124, 131, 138, 145, 152, 159, 166]


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    # This is for main choices, each variable is one row in the choice table MPL
    C_demo = models.CharField(
        choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal, blank=True)
    C_1 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_2 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_3 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_4 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_5 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_6 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_7 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_8 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_9 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    C_10 = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    # This is needed for the instructions
    C = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    # This for feedback
    random_row = models.IntegerField()
    random_value = models.IntegerField()
    choice_sel = models.CharField()
    # Control quesitonnaire
    CQ_1 = models.CharField(
        choices=[["A",gettext("100 tokens in 2 weeks")], ["B",gettext("100 tokens in 4 weeks")], ["C",gettext('105 tokens in 4 weeks')], ["D",gettext("105 tokens in 2 weeks")]], widget=widgets.RadioSelect)
    CQ_2 = models.CharField(
        choices=[["A",gettext("124 tokens in 2 weeks")], ["B",gettext("124 tokens in 4 weeks")], ["C",gettext('100 tokens in 4 weeks')], ["D",gettext("100 tokens in 2 weeks")]], widget=widgets.RadioSelect)
    # These variables are collected in the final questionnaire
    Q_1 = models.CurrencyField()
    Q_2 = models.CharField(choices=['Yes', "No"], widget=widgets.RadioSelectHorizontal)
    Q_3 = models.IntegerField(
        choices=[
            [1,gettext("Not at all")],
            [2, gettext("Little")],
            [3, gettext("Average")],
            [4, gettext("Fairly well")],
            [5, gettext("Very well")],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    Q_4 = models.IntegerField(
        choices=[
            [1, gettext("Not at all")],
            [2, gettext("Little")],
            [3, gettext("Average")],
            [4, gettext("Some trust")],
            [5, gettext("A lot of trust")],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    # Define here the methods associated to Players
    # this method is needed to compute payoffs


# FUNCTIONS

def creating_session(subsession: Subsession):
    for g in subsession.get_groups():
        for p in g.get_players():
            # to play outside blocks
            try:
                if p.session.config['block'] == "block1":
                    continue
            except:
                p.participant.vars['game_count'] = 0
                
def set_payoff(player: Player):
    # *******************************************
    # select random row and random outcome
    # *******************************************
    row = random.randint(1, 10)
    # select one row randomly for payment (from module random)
    # *******************************************
    # select choices in correspondence to random row
    # *******************************************
    choices = [
        player.C_1,
        player.C_2,
        player.C_3,
        player.C_4,
        player.C_5,
        player.C_6,
        player.C_7,
        player.C_8,
        player.C_9,
        player.C_10,
    ]
    # create a list with all choices of the player (see self)
    choice_sel = choices[row - 1]
    # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
    # *******************************************
    # Compute here the payoffs
    # *******************************************
    if choice_sel == "A":  # A, closer in time
        # if the choice was A
        earnings = Constants.A
    else:
        # if the choice was B
        earnings = Constants.B[row - 1]
    player.payoff = earnings
    player.random_row = row
    player.choice_sel = choice_sel
    #save for later
    player.participant.vars['TIME_info'] = [
        player.choice_sel, player.random_row, player.payoff]  # for later


def update_counter(group: Group):
    for p in group.get_players():
        p.participant.vars['game_count'] += 1

# PAGES
class Instructions(Page):
    pass
    # form_model = 'player'
    # form_fields = ['C'] # the demo MPL

    def vars_for_template(player: Player):
        return {
            'counter': player.participant.vars['game_count']
        }

class Choices(Page):
    # which forms are needed from class player
    form_model = 'player'
    # all 10 options,
    form_fields = ['C_1', 'C_2', 'C_3', 'C_4', 'C_5', 'C_6', 'C_7', 'C_8', 'C_9', 'C_10']
    # values that are to be displayed (dictionary)
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from constants and store them in a dictionary
        return {
            'A': Constants.A,
            'B_1': Constants.B[0],
            'B_2': Constants.B[1],
            'B_3': Constants.B[2],
            'B_4': Constants.B[3],
            'B_5': Constants.B[4],
            'B_6': Constants.B[5],
            'B_7': Constants.B[6],
            'B_8': Constants.B[7],
            'B_9': Constants.B[8],
            'B_10': Constants.B[9],
        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # built-in method
        set_payoff(player)  # see in models in Player class


class Example(Page):
    pass
    form_model = 'player'
    # all 10 options,
    form_fields = ['C_demo','CQ_1','CQ_2']

    def error_message(player: Player, values):
        if values["CQ_1"] != "A":
            return gettext('Please check your answer to question 1')

        if values["CQ_2"] != "B":
            return gettext('Please check your answer to question 2')

class Outcome(Page):
    pass
    # values needed to inform subjects about the actual outcome
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from participant.vars and store them in a dictionary
        return dict(
            payoff=player.payoff,  # payoff
            row=player.random_row,  # randomly chosen row
            choice=player.choice_sel,  # actual choice
        )
        
    def is_displayed(player: Player):  # display only if it is not in block
        try:
            return player.session.config['block'] != "block1" and player.session.config['block'] != "block2"
        except:
            return True

class Questionnaire(Page):
    pass
    # forms to retrieve individual information
    form_model = 'player'
    form_fields = ['Q_1', 'Q_3', 'Q_4']  #


# 1) What amount of money would you be willing to receive six months from now to save the 100 tokens today?
# 2) If you were offered a loan of 1000 tokens today, but you would have to repay 1100 tokens in four months, would you borrow the money?
# 3) How much do you think that you understood the instructions of the game? (Code)
# 4) How much do you trust that you will receive the money in 2 or 4 weeks’ time? (Code)
# Code: 1 = Very little; 2 = Little 3 = Average; 4 = Good; 5 = Very good.

class ChoiceWaitPageInit(WaitPage):
    # update counter
    after_all_players_arrive = 'update_counter'
    wait_for_all_groups = True

class Header(Page):
    timeout_seconds = 5

    def vars_for_template(player: Player):

        return {
            'counter': player.participant.vars['game_count']
        }

# the coreography of pages
page_sequence = [ChoiceWaitPageInit, Header, Instructions, Example,
                 Choices, Questionnaire, Outcome]
