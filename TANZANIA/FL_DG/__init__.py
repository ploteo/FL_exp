from otree.api import *
import random
from gettext import gettext

doc = """
DG
- 1 round

"""


class Constants(BaseConstants):
    name_in_url = 'FL_DG'
    players_per_group = 2
    num_rounds = 1
    endowment_sender = cu(100)
    endowment_receiver = cu(0)
    multiplier = 3
    institutions = ["A", "B"] # here the names of the insitution
  

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    choice_sender = models.CurrencyField()
    payoff_sender = models.CurrencyField()
    payoff_receiver = models.CurrencyField()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    institution = models.CharField()# to retrieve the instiution
    sent = models.CurrencyField(min=0, max=Constants.endowment_sender)
    sent_inst = models.CurrencyField(min=0, max=Constants.endowment_sender) # amount sent to the institution
    type = models.CharField()
    Q1 = models.CurrencyField()
    Q2 = models.CurrencyField()
    Q3 = models.CurrencyField()

    FQ1 = models.IntegerField()
    FQ2 = models.CharField(
        widget=widgets.RadioSelectHorizontal, label="", choices=[
            gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Fairly Well"), gettext("Completely")]
    )
    FQ3 = models.CharField(widget=widgets.RadioSelectHorizontal, label="", choices=[
        gettext("Not at all"), gettext("Little"), gettext("Average"), gettext("Fairly Well"), gettext("Very well")])

# def returned_max(group: Group):
#     return group.choice_sender*Constants.multiplier
# FUNCTIONS
def creating_session(subsession: Subsession):
    subsession.group_randomly()
    for g in subsession.get_groups():
        for p in g.get_players():
            # retrieve institution information
            p.institution = str(p.participant.vars['institution']["Inst_Name"])
            if p.id_in_group % 2 == 1:
                p.type = 'sender'
                p.endowment = Constants.endowment_sender
            elif p.id_in_group % 2 == 0:
                p.type = 'receiver'
                p.endowment = Constants.endowment_receiver
    # to play outside blocks
            try:
                if p.session.config['block'] == "block1": 
                    continue  
            except:
                p.participant.vars['game_count'] = 0

def set_payoffs(group: Group):  # choice of sender
    players = group.get_players()
    for p in players:
        if p.type == "sender":
            group.choice_sender = p.sent
    group.payoff_sender = Constants.endowment_sender - group.choice_sender
    group.payoff_receiver = Constants.endowment_receiver + group.choice_sender
    # write payoffs
    for p in players:
        if p.type == "sender":
            p.payoff = group.payoff_sender
        else:
            p.payoff = group.payoff_receiver
        # for later when we pay everything at the end
        p.participant.vars['DG_info'] = [Constants.endowment_sender,p.type, p.payoff, group.choice_sender, p.sent_inst]

def update_counter(group: Group) :
    for p in group.get_players():
        p.participant.vars['game_count'] += 1

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PAGES
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Instructions_container(Page):

    def is_displayed(player: Player):
        return player.round_number == 1
    
    def vars_for_template(player: Player):
        return {
            'counter': player.participant.vars['game_count']
        }

class Questionnaire_1(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3']

    def is_displayed(player: Player):
        return player.round_number == 1

    def error_message(player: Player, values):
        if values["Q1"] != 100:
            return gettext('Please check your answer to question 1')
        if values["Q2"] != 100:
            return gettext('Please check your answer to question 2')
        if values["Q3"] != 50:
            return gettext('Please check your answer to question 3')


class Choice_sender(Page):
    form_model = 'player'
    form_fields = ['sent']


class Choice_sender_inst(Page):
    form_model = 'player'
    form_fields = ['sent_inst']

    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"]
        }

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'type': player.type,
            'sent': player.group.choice_sender,
            'payoff_sender': player.group.payoff_sender,
            'payoff_receiver': player.group.payoff_receiver,
            'sent_inst': player.sent_inst,
            'payoff_sender_inst': Constants.endowment_sender-player.sent_inst,
            'payoff_tot': player.payoff+Constants.endowment_sender-player.sent_inst
        }

    def is_displayed(player: Player):  # display only if it is not in block
        try:
            return player.session.config['block'] != "block1"
        except:
            return True


class Instructions_sender_inst(Page):

    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"]
        }
class ChoiceWaitPage1(WaitPage):
    after_all_players_arrive = 'set_payoffs'  # retrieve values (A)


class ChoiceWaitPageInit(WaitPage):
    # update counter
    after_all_players_arrive = 'update_counter'
    wait_for_all_groups = True


class inst_descr(Page):

    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"],
            'Product': player.participant.vars['institution']["Inst_Product"],
        }

class Header(Page):
    timeout_seconds = 5

    def vars_for_template(player: Player):
        return {
            'counter': player.participant.vars['game_count']
        }

class Final_questionnaire(Page):
    form_model = 'player'
    form_fields = ['FQ1', 'FQ2', 'FQ3']

    def vars_for_template(player: Player):
        return{
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'Type': player.participant.vars['institution']["Inst_Type"],
            'Area': player.participant.vars['institution']["Inst_Area"]
        }


page_sequence = [ChoiceWaitPageInit,  Header, Instructions_container, Questionnaire_1, Choice_sender,
                 Instructions_sender_inst, inst_descr, Choice_sender_inst, ChoiceWaitPage1, Results, Final_questionnaire]
