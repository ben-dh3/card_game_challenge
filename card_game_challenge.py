from random import shuffle

class Card():
    def __init__(self):
        self=self
        self.cards=[]
        self.players_hand={}
        self.played_cards={}
    def shuffle(self):
        self.cards=['SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
            'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
            'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',
            'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK']
        shuffle(self.cards)
        return self.cards
    # 3 or 4 players
    def deal(self,number_of_players):
        split_cards=int(52/number_of_players)
        break1=0
        break2=split_cards
        for i in range(1,number_of_players+1):
                self.players_hand[f'player{i}']=self.cards[break1:break2]
                break1+=split_cards
                break2+=split_cards
        return self.players_hand
    
    def play_cards(self,p1_choice,p2_choice,p3_choice,p4_choice=None,):

        if p1_choice in self.players_hand['player1']:
            self.played_cards['player1']=p1_choice
        elif p1_choice not in self.players_hand['player1']:
            self.played_cards['player1']=self.players_hand['player1'][0]
            
        if p2_choice in self.players_hand['player2']:    
            self.played_cards['player2']=p2_choice
        elif p2_choice not in self.players_hand['player2']:
            self.played_cards['player2']=self.players_hand['player2'][0]

        if p3_choice in self.players_hand['player3']:
            self.played_cards['player3']=p3_choice
        elif p3_choice not in self.players_hand['player3']:
            self.played_cards['player3']=self.players_hand['player3'][0]  

        if p4_choice:  
            if p4_choice in self.players_hand['player4']:
                self.played_cards['player4']=p4_choice
            elif p4_choice not in self.players_hand['player4']:
                self.played_cards['player4']=self.players_hand['player4'][0]    
        return self.played_cards
    
card=Card()
print(card.shuffle())
print(card.deal(4))
print(card.play_cards('C6','C7','H9','C9'))