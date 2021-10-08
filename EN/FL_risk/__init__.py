import random
from gettext import gettext
from otree.api import *


author = 'M. Ploner'
doc = """
    MPL risk elicitation à la Holt&Laury
"""


class Constants(BaseConstants):
    name_in_url = 'MPL'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    Ah = 100
    Al = 80
    Bh = 190
    Bl = 5


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
    # COntro questions
    CQ_1 = models.IntegerField(
        choices=[[100, gettext('100 tokens')], [80, gettext('80 tokens')], [5, gettext("5 tokens")],  [190, gettext("190 tokens")]], widget=widgets.RadioSelect)
    CQ_1b = models.IntegerField(
        choices=[[100, gettext('100 tokens')], [80, gettext('80 tokens')], [5, gettext("5 tokens")],  [190, gettext("190 tokens")]], widget=widgets.RadioSelect)
    CQ_2 = models.IntegerField(
        choices=[[100, gettext('100 tokens')], [80, gettext('80 tokens')], [5, gettext("5 tokens")],  [190, gettext("190 tokens")]], widget=widgets.RadioSelect)
    CQ_2b =models.IntegerField(
        choices=[[100, gettext('100 tokens')], [80, gettext('80 tokens')], [5, gettext("5 tokens")],  [190, gettext("190 tokens")]], widget=widgets.RadioSelect)
        # questionnaire
    Q_1 = models.IntegerField(
        choices=[
            [1, gettext("Not at all")],
            [2, gettext("Little")],
            [3, gettext("Average")],
            [4, gettext("Fairly well")],
            [5, gettext("Very well")],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    # This is needed for the instructions
    C = models.CharField(choices=[["A", 'A'], ["B", 'B']], widget=widgets.RadioSelectHorizontal)
    # This for feedback
    random_row = models.IntegerField()
    random_value = models.IntegerField()
    choice_sel = models.CharField()
    # These variables are collected in the final questionnaire
    sex = models.StringField(widget=widgets.RadioSelectHorizontal(), choices=[gettext('Male'), gettext('Female')])
    age = models.IntegerField(choices=range(18, 60, 1))
    comment = models.TextField(label="Your comment here:")
    like = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
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
    x = random.randint(1, 10)
    # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
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
    if x <= row:
        # if the random number is smaller equal than the random row
        if choice_sel == "A":  # A
            # if the choice was A
            earnings = Constants.Ah
            # because HL_row is the same as p in the MPL
        else:
            # if the choice was B
            earnings = Constants.Bh
    else:
        # if the random number is slarger than the random row
        if choice_sel == "A":  # A
            # if the choice was A
            earnings = Constants.Al
            # because HL_row is the same as p in the MPL
        else:
            earnings = Constants.Bl
    player.payoff = earnings
    player.random_row = row
    player.random_value = x
    player.choice_sel = choice_sel
    # save for later
    player.participant.vars['RISK_info'] = [player.random_row, player.random_value, player.choice_sel, player.payoff, Constants.Ah, Constants.Al, Constants.Bh,Constants.Bl]


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
        return {}

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # built-in method
        set_payoff(player)  # see in models in Player class


class Outcome(Page):
    pass
    # values needed to inform subjects about the actual outcome
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from participant.vars and store them in a dictionary
        return dict(
            payoff=player.payoff,  # payoff
            row=player.random_row,  # randomly chosen row
            value=player.random_value,  # randomly chosen value to define outcome
            choice=player.choice_sel,  # actual choice
            image_path='FL_risk/LOTT_{}.png'.format(player.random_row),
        )

    def is_displayed(player: Player):  # display only if it is not in block
        try:
            return player.session.config['block'] != "block1" and player.session.config['block'] != "block2"
        except:
            return True

class Anag(Page):
    pass
    # forms to retrieve individual information
    form_model = 'player'
    form_fields = ['comment', 'like', 'sex', 'age']  # plyaer.comment, player.like, ...

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

class Example(Page):
    form_model = 'player'
    # all 10 options,
    form_fields = ['C_demo','CQ_1', 'CQ_2','CQ_1b','CQ_2b']

    def error_message(player: Player, values):
        if values["CQ_1"] != 80:
            return gettext('Please check your answer to question 1a')
        if values["CQ_1b"] != 5:
            return gettext('Please check your answer to question 1b')
        if values["CQ_2"] != 190:
            return gettext('Please check your answer to question 2a')
        if values["CQ_2b"] != 100:
            return gettext('Please check your answer to question 2b')

class Questionnaire(Page):
    pass
    # forms to retrieve individual information
    form_model = 'player'
    form_fields = ['Q_1']  #

# the coreography of pages
page_sequence = [ChoiceWaitPageInit, Header, Instructions, Example,  Choices, Outcome, Questionnaire]
