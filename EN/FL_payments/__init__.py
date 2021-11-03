import datetime
from datetime import date

from otree.api import *


doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'FL_payments'
    players_per_group = None
    num_rounds = 1
    today = date.today()
    start = datetime.datetime.strptime(str(today), "%Y-%m-%d")
    today_2 = str(start + datetime.timedelta(days=14))[0:10]
    today_4 = str(start + datetime.timedelta(days=28))[0:10]

class Subsession(BaseSubsession):
    exch_rate = models.FloatField()
    show_up = models.RealWorldCurrencyField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # to display them in the data
    payoff_DG = models.CurrencyField()
    payoff_TG = models.CurrencyField()
    payoff_PGG = models.CurrencyField()
    payoff_risk = models.CurrencyField()
    payoff_time = models.CurrencyField()
    payoff_TOT = models.CurrencyField()
    payoff_TOT_now = models.CurrencyField()

# FUNCTIONS

def creating_session(subsession: Subsession):
    subsession.exch_rate = subsession.session.config['real_world_currency_per_point']
    subsession.show_up = int(subsession.session.config['participation_fee'])

# PAGES
class MyPage(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class Results_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['block'] == "block1"

    @staticmethod
    def vars_for_template(player: Player):
        payoff_DG1 = cu(player.participant.vars['DG_info'][2])
        payoff_DG2 = cu(player.participant.vars['DG_info'][0] -player.participant.vars['DG_info'][4])
        payoff_TG1 = cu(player.participant.vars['TG_info'][1])
        payoff_TG2 = cu(player.participant.vars['TG_info'][8])
        payoff_Risk = cu(player.participant.vars['RISK_info'][3])
        payoff_Time = cu(player.participant.vars['TIME_info'][2])

        # print(payoff_DG1)
        # print(payoff_DG2)
        # print(payoff_TG1)
        # print(payoff_TG2)
        # print(payoff_Time)
        # print(payoff_Risk)

        total_pay = (
            payoff_DG1+
        payoff_DG2+
        payoff_TG1+
        payoff_TG2+
        payoff_Risk+
        payoff_Time
        )
# to display them in the DB (for payment purposes)
        player.payoff_DG = payoff_DG1+payoff_DG2
        player.payoff_TG = payoff_TG1+ payoff_TG2
        player.payoff_risk = payoff_Risk
        player.payoff_time = payoff_Time
        player.payoff_TOT = total_pay
        player.payoff_TOT_now = total_pay - payoff_Time

        player.participant.payoff = total_pay - payoff_Time  # to use the payment form (subtract deferred pay)

        return {
            'show_up': player.subsession.session.config['participation_fee'],
            'block': 1,
            #DG
            'type': player.participant.vars['DG_info'][1],
            'sent': player.participant.vars['DG_info'][3],
            'payoff_sender': player.participant.vars['DG_info'][0]-player.participant.vars['DG_info'][3],
            'payoff_receiver': player.participant.vars['DG_info'][3],
            'sent_inst': player.participant.vars['DG_info'][4],
            'payoff_sender_inst': player.participant.vars['DG_info'][0]-player.participant.vars['DG_info'][4],
            'payoff_tot': player.participant.vars['DG_info'][2]+player.participant.vars['DG_info'][0]-player.participant.vars['DG_info'][4],
            #TG
            'type_TG': player.participant.vars['TG_info'][0],
            'payoff': player.participant.vars['TG_info'][1],
            'amount_sender_TG': cu(player.participant.vars['TG_info'][2]),
            'amount_received_TG': cu(player.participant.vars['TG_info'][3]),
            'amount_receiver_TG': player.participant.vars['TG_info'][4],
            'Institution': player.participant.vars['institution']["Inst_Name"],
            'trust_inst': cu(player.participant.vars['TG_info'][6]),
            'recipr_institution': player.participant.vars['TG_info'][7],
            'payoff_inst': player.participant.vars['TG_info'][8],
            'payoff_tot_TG': player.participant.vars['TG_info'][1]+player.participant.vars['TG_info'][8],
            #RISK
            'Payoff_risk': player.participant.vars['RISK_info'][3],
            'row_risk': player.participant.vars['RISK_info'][0],
            'value': player.participant.vars['RISK_info'][1],
            'choice_risk': player.participant.vars['RISK_info'][2],
            'Ah': player.participant.vars['RISK_info'][4],
            'Al': player.participant.vars['RISK_info'][5],
            'Bh': player.participant.vars['RISK_info'][6],
            'Bl': player.participant.vars['RISK_info'][7],
            'image_path': 'FL_risk/LOTT_{}.png'.format(player.participant.vars['RISK_info'][0]),
            #TIME
            'payoff_time': player.participant.vars['TIME_info'][2],
            'row': player.participant.vars['TIME_info'][1],
            'choice_time': player.participant.vars['TIME_info'][0],
            #TOTAL
            'Total_payment': total_pay,
            'Total_payment_exc': round(float(total_pay) * player.subsession.exch_rate, 2),
            'Total_payment_now': total_pay-payoff_Time,
            'Total_payment_now_exc': round(float(total_pay-payoff_Time) * player.subsession.exch_rate, 2),
            'Total_payment_late_exc': round(float(payoff_Time) * player.subsession.exch_rate, 2)
        }
 
 
class Results_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['block'] == "block2"

    @staticmethod
    # to be defined here

    def vars_for_template(player: Player):  
        print(player.participant.vars['PGG_info']) #need to retrieve this info
        payoff_PGG_1 = player.participant.vars['PGG_info'][3][0]
        payoff_PGG_2 = player.participant.vars['PGG_info'][3][1]
        payoff_Risk = cu(player.participant.vars['RISK_info'][3])
        payoff_Time = cu(player.participant.vars['TIME_info'][2])

        total_pay = (payoff_PGG_1+payoff_PGG_2+
        payoff_Risk+
        payoff_Time
        )
# to display them in the DB (for payment purposes)
        player.payoff_PGG = payoff_PGG_1+payoff_PGG_2
        player.payoff_risk = payoff_Risk
        player.payoff_time = payoff_Time
        player.payoff_TOT = total_pay
        player.payoff_TOT_now = total_pay - payoff_Time
        
        # to use the payment form (subtract the time payoff)
        player.participant.payoff = total_pay - payoff_Time

        return {
            'show_up': player.subsession.session.config['participation_fee'],
            'block': 2,
            # PGG
            'endowment_1': player.participant.vars['PGG_info'][0][0],
            'endowment_2': player.participant.vars['PGG_info'][0][1],
            'own_contribution_1': player.participant.vars['PGG_info'][1][0],
            'own_contribution_2': player.participant.vars['PGG_info'][1][1],
            'total_contributions_1': player.participant.vars['PGG_info'][2][0],
            'total_contributions_2': player.participant.vars['PGG_info'][2][1],
            'payoff_PGG_1': player.participant.vars['PGG_info'][3][0],
            'payoff_PGG_2': player.participant.vars['PGG_info'][3][1],
            #RISK
            'Payoff_risk': player.participant.vars['RISK_info'][3],
            'row_risk': player.participant.vars['RISK_info'][0],
            'value': player.participant.vars['RISK_info'][1],
            'choice_risk': player.participant.vars['RISK_info'][2],
            'Ah': player.participant.vars['RISK_info'][4],
            'Al': player.participant.vars['RISK_info'][5],
            'Bh': player.participant.vars['RISK_info'][6],
            'Bl': player.participant.vars['RISK_info'][7],
            'image_path': 'FL_risk/LOTT_{}.png'.format(player.participant.vars['RISK_info'][0]),
            #TIME
            'payoff_time': player.participant.vars['TIME_info'][2],
            'row': player.participant.vars['TIME_info'][1],
            'choice_time': player.participant.vars['TIME_info'][0],
            #TOTAL
            'Total_payment': total_pay,
            'Total_payment_exc': round(float(total_pay) * player.subsession.exch_rate,2),
            'Total_payment_now': total_pay-payoff_Time,
            'Total_payment_now_exc': round(float(total_pay-payoff_Time) * player.subsession.exch_rate, 2),
            'Total_payment_late_exc': round(float(payoff_Time) * player.subsession.exch_rate, 2)
               }


class End(Page):
    pass

page_sequence = [ResultsWaitPage, Results_1, Results_2]
