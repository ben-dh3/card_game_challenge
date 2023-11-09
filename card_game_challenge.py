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
        for player,hand in self.players_hand.items():
            if 'C2' in hand:
                self.played_cards[player]='C2'
            else:
                for suit in hand:
                    if suit[0]!='C':
                        self.played_cards[player]=suit
                    if suit[0]== 'C':
                        self.played_cards[player]=suit
                        break

        return self.played_cards
    
card=Card()
card.shuffle()
print(card.deal(4))
print(card.play_cards('C6','C7','H9','C9'))