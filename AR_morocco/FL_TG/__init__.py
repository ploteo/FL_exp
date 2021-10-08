import csv
from otree.api import *
from gettext import gettext
import random

doc = """
mini TG

4 levels of trust: 0, 30, 60, 90

## STAGE 1
- Either choose as trustor or as trustee
- Assign roles randomly

## STAGE 2
- Choose as trustor vs a representative of the NGO

"""


class Constants(BaseConstants):
    name_in_url = 'FL_TG'
    players_per_group = 2
    num_rounds = 1
    endowment = cu(100)
    choices_sender = [0,25,50,75,100]
    multiplier = 3
    instructions_welcome = 'FL_TG/Instructions_welcome.html'


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    choice_sender = models.CurrencyField()
   
    choice_receiver = models.CurrencyField()

    payoff_sender = models.CurrencyField()
    payoff_receiver = models.CurrencyField()
    

class Player(BasePlayer):
    endowment = models.CurrencyField()
    type = models.CharField()
    payoff_inst = models.CurrencyField()
    institution = models.CharField()  # to retrieve the instiution

    # the amount given to other as trust
    trust = models.CurrencyField(
        choices=[[0, '0'], [1, '25'], [2, '50'], [3, '75'], [4,'100']], widget=widgets.RadioSelect)

    trust_inst = models.CurrencyField(
        choices=[[0, '0'], [1, '25'], [2, '50'], [3, '75'], [4,'100']], widget=widgets.RadioSelect)

    recipr_0 = models.CurrencyField(initial=0)  # the amount returned for trust 0
    recipr_1 = models.CurrencyField(min=0)  # the amount returned for trust 1
    recipr_2 = models.CurrencyField(min=0)  # the amount returned for trust 2
    recipr_3 = models.CurrencyField(min=0)  # the amount returned for trust 3
    recipr_4 = models.CurrencyField(min=0)  # the amount returned for trust 4

    recipr_inst = models.CurrencyField()

# Questionnaire
    Q1_1 = models.CurrencyField()
    Q1_2 = models.CurrencyField()
    Q2_1 = models.CurrencyField()
    Q2_2 = models.CurrencyField()
    Q3_1 = models.CurrencyField()

    # Final questionnaire
    FQ_1 = models.CharField(label="", widget=widgets.RadioSelect, choices=[
                            gettext('I decided based on expectation of similar or larger  donation'), gettext('I decided the amount without expecting a larger donation in return or independently from the donation the receiver would send me in. '),gettext('Others(specify)')])
    FQ_1b = models.LongStringField(blank=True)
    FQ_1c = models.CurrencyField()
    FQ_2 = models.CurrencyField(choices=[[0, '0'], [1, '25'], [2, '50'], [3, '75'], [4, '100']], widget=widgets.RadioSelect)
    FQ_2b = models.CharField(label="", widget=widgets.RadioSelect, choices=[gettext('Yes'), gettext('No'), gettext('I do not know')])
    FQ_3 = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Fairy Well"), gettext("Very well")])

    
    FQinst_1 = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[
     gettext('I decided based on expectation of similar or larger  donation'), gettext('I decided the amount without expecting a larger donation in return or independently from the donation the receiver would send me in. ')])
    FQinst_2 = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[
    gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Quite"), gettext("Very")])
    FQinst_3 = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[
        gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Fairy Well"), gettext("Very well")])

        #added this after Ginevra's suggestion
    FQinst_4 = models.CharField()
    # if participant.vars['institution']["Inst_Type"] == "NGO":
# FQinst_4ngo = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[
#     gettext("Eco-friendly solutions"), gettext("Nutrient-dense food products"), gettext("Medical care")])  #NGO 
# FQinst_4assoc = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[
#     gettext("Eco-friendly solutions"), gettext("Nutrient-dense food products"), gettext("Micro finance")]) #Association

# def returned_max(group: Group):
#     return group.choice_sender*Constants.multiplier
# FUNCTIONS
def creating_session(subsession: Subsession):
    subsession.group_randomly()
    for g in subsession.get_groups():
        for p in g.get_players():
            # retrieve institution information
            p.institution = str(p.participant.vars['institution']["Inst_Name"])# Insitution name
            if p.id_in_group == 1:  # sender
                p.type = "sender"
            if p.id_in_group == 2:  # receiver
                p.type = "receiver"
    # to play outside blocks
            try:
                if p.session.config['block'] == "block1":
                    continue
            except:
                p.participant.vars['game_count'] = 0
## PAYOFFS

def set_payoffs(group: Group):  # choice of responder

    group.choice_sender = group.get_player_by_id(1).trust

    choices_receiver = [group.get_player_by_id(2).recipr_0,group.get_player_by_id(2).recipr_1,group.get_player_by_id(2).recipr_2,group.get_player_by_id(2).recipr_3,group.get_player_by_id(2).recipr_4]
    group.choice_receiver = choices_receiver[int(group.choice_sender)]

    players = group.get_players()
    for p in players:
        if p.type == "sender":
            p.payoff = Constants.endowment - Constants.choices_sender[int(group.choice_sender)] + group.choice_receiver
        if p.type == "receiver":
            p.payoff = Constants.endowment + Constants.choices_sender[int(group.choice_sender)]*Constants.multiplier - group.choice_receiver
        #store for later payment
        p.participant.vars['TG_info'] = [p.type, p.payoff, Constants.choices_sender[int(group.choice_sender)], Constants.choices_sender[int(group.choice_sender)]*Constants.multiplier, group.choice_receiver]

def set_payoffs_inst(player: Player):  # choice of responder

    list_choices_inst = [
                        cu(player.participant.vars['institution_choices']
                            ["Choice_other_0"]),
                         cu(player.participant.vars['institution_choices']
                            ["Choice_other_25"]),
                         cu(player.participant.vars['institution_choices']
                            ["Choice_other_50"]),
                         cu(player.participant.vars['institution_choices']
                            ["Choice_other_75"]),
                        cu(player.participant.vars['institution_choices']
                            ["Choice_other_100"])                            
                        ]

    player.recipr_inst = list_choices_inst[int(player.trust_inst)]
    player.payoff_inst = Constants.endowment - \
        Constants.choices_sender[int(player.trust_inst)] + \
                        player.recipr_inst
    #store for later payment
    player.participant.vars['TG_info'].extend(
        [Constants.endowment, cu(Constants.choices_sender[int(player.trust_inst)]), player.recipr_inst, player.payoff_inst]
        )

def update_counter(group: Group):
    for p in group.get_players():
        p.participant.vars['game_count'] += 1
#================================================================
# PAGES
#================================================================

class Instructions_container(Page):

    def is_displayed(player: Player):
        return player.round_number == 1

    def vars_for_template(player: Player):
        return {
            'counter': player.participant.vars['game_count']
        }

class Questionnaire_1(Page):
    form_model = 'player'
    form_fields = ['Q1_1', 'Q1_2', 'Q2_1', 'Q2_2', 'Q3_1']

    def is_displayed(player: Player):
        return player.round_number == 1

    def error_message(player: Player, values):
        if values["Q1_1"] != 100:
            return gettext('Please check your answer to question 1a')

        if values["Q1_2"] != 0:
            return gettext('Please check your answer to question 1b')

        if values["Q2_1"] != 175:
            return gettext('Please check your answer to question 2a')

        if values["Q2_2"] != 75:
            return gettext('Please check your answer to question 2b')

        if values["Q3_1"] != 150:
            return gettext('Please check your answer to question 3a')

class Instructions_sender(Page):

    @staticmethod
    def vars_for_template(player: Player):

        return {
            'l1': int(Constants.choices_sender[0]),
            'l2': cu(Constants.choices_sender[1]),
            'l3': cu(Constants.choices_sender[2]),
            'l4': cu(Constants.choices_sender[3])
        }

class Instructions_receiver(Page):
    pass


class Instructions_sender_inst(Page):
    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"]
        }
class Choice_sender(Page):
    form_model = 'player'
    form_fields = ['trust']

    # def is_displayed(player: Player):
    #     return player.type == "sender"

class Choice_sender_inst(Page):
    form_model = 'player'
    form_fields = ['trust_inst']

    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"]
        }

    def before_next_page(player, timeout_happened):
        set_payoffs_inst(player)

class Choice_receiver(Page):
    form_model = 'player'
    form_fields = ['recipr_1', 'recipr_2', 'recipr_3','recipr_4']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            # Amount sent
            'trustor_0': Constants.choices_sender[0],
            'trustor_1': Constants.choices_sender[1],
            'trustor_2': Constants.choices_sender[2],
            'trustor_3': Constants.choices_sender[3],
            'trustor_4': Constants.choices_sender[4],
            # Amount received
            'trustor_0_received': Constants.choices_sender[0] * Constants.multiplier,
            'trustor_1_received': Constants.choices_sender[1] * Constants.multiplier,
            'trustor_2_received': Constants.choices_sender[2] * Constants.multiplier,
            'trustor_3_received': Constants.choices_sender[3] * Constants.multiplier,
            'trustor_4_received': Constants.choices_sender[4] * Constants.multiplier
        }

    @staticmethod
    def error_message(player: Player, value):
        if value["recipr_1"] > Constants.choices_sender[1] * Constants.multiplier:
            return 'In Choice #2, you cannot send more than what you received'
        if value["recipr_2"] > Constants.choices_sender[2] * Constants.multiplier:
            return 'In Choice #3, you cannot send more than what you received'
        if value["recipr_3"] > Constants.choices_sender[3] * Constants.multiplier:
            return 'In Choice #4, you cannot send more than what you received'
        if value["recipr_4"] > Constants.choices_sender[4] * Constants.multiplier:
            return 'In Choice #5, you cannot send more than what you received'

    # def is_displayed(player: Player):
    #     return player.type == "receiver"

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'payoff': player.payoff,
            'amount_sender': cu(Constants.choices_sender[int(player.group.choice_sender)]),
            'amount_received': cu(Constants.choices_sender[int(player.group.choice_sender)]*Constants.multiplier),
            'amount_receiver': player.group.choice_receiver,
            'trust_inst': cu(Constants.choices_sender[int(player.trust_inst)]),
            'recipr_institution': player.recipr_inst,
            'payoff_inst': player.payoff_inst,
            'player_tot_payoff': player.payoff_inst+player.payoff

        }

    def is_displayed(player: Player):  # display only if it is not in block
        try:
            return player.session.config['block']!="block1" 
        except:
            return True


class ChoiceWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'  # retrieve values


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

class Final_questionnaire_sender(Page):
    form_model = 'player'
    form_fields = ['FQ_1', 'FQ_1b', 'FQ_1c', 'FQ_3']

    @staticmethod
    def error_message(player: Player, value):
        if value["FQ_1"] == "Others(specify)" and value["FQ_1b"] == "":
            return gettext('If you chose Others in question 1 you must specify how you decided')

    # def is_displayed(player: Player):
    #     return player.type == "sender"

class Final_questionnaire_receiver(Page):
    form_model = 'player'
    form_fields = ['FQ_2', 'FQ_2b']

    # def is_displayed(player: Player):
    #     return player.type == "receiver"
    
    @staticmethod
    def error_message(player: Player, value):
        if value["FQ_2"] == "Yes" and value["FQ_2b"] == "-99":
            return gettext('If you chose yes in question 1 you must specify the level of disappointment')


class Final_questionnaire_inst(Page):
    form_model = 'player'
    form_fields = ['FQinst_1', 'FQinst_2','FQinst_3','FQinst_4']

    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"],
            'Product': player.participant.vars['institution']["Inst_Product"],
            'Tag': player.participant.vars['institution']["Tag"]
        }


class inst_descr(Page):
    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"],
            'Product': player.participant.vars['institution']["Inst_Product"]
        }


page_sequence = [ChoiceWaitPageInit, Header, Instructions_container, Questionnaire_1, Choice_sender, Choice_receiver, Final_questionnaire_sender, Final_questionnaire_receiver,ChoiceWaitPage, Instructions_sender_inst, inst_descr, Choice_sender_inst, Results, Final_questionnaire_inst]
