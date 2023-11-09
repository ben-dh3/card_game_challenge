from random import shuffle

class Card():
    def __init__(self):
        self=self
        self.players=[]
        self.cards=[]

    def shuffle_and_deal(self):
        self.players=['player1','player2','player3','player4']
        self.cards=['SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
            'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
            'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',
            'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK']
        shuffle(self.cards)
        players_hand={}
        players_hand['player1']=self.cards[:13]
        players_hand['player2']=self.cards[13:26]
        players_hand['player3']=self.cards[26:39]
        players_hand['player4']=self.cards[39:52]
        # players_hand={player:card for (player,card) in zip(self.players,self.cards)}
        return players_hand

card=Card()

print(card.shuffle_and_deal())