from random import randint

class Person(object):
    def __init__(self):
        
        self.cards = []
        
        
    def clear_hand(self):
        
        self.cards = []
        
        
    def get_card(self, card):
        
        self.cards.append(card)
        
        
    def count_cards(self, ace_is_one = False):
        
        count = 0
        
        l = list(self.cards)
        if (l.count('A') > 0):
            
            while (l.index('A') < (len(l) - l.count('A'))):
                l.append(l.pop(l.index('A')))
                   
        for x in xrange(len(l)):
            
            try:
                
                c = int(l[x])
                
            except:
                
                if (l[x] == 'A'):
                    
                    if ((count + 11 > 21) or (ace_is_one == True)):
                        c = 1
                    else:
                        c = 11
                        
                else:
                    c = 10
                    
            finally:
                
                count += c
        
        if ((count > 21) and (l.count('A') > 1) and (ace_is_one == False)):
            return self.count_cards(ace_is_one = True)
        else:
            return count
        
    def card_string(self):
        
        s = ""
        for x in xrange(len(self.cards)-1):
            
            s += self.cards[x] + ", "
        
        s += self.cards[-1]
        
        return s

class Player(Person):
    
    def __init__(self, bankroll=100):
        
        Person.__init__(self)
        self.bankroll = bankroll
        
    def add_bankroll(self, amount):
        
        self.bankroll += amount
    
    def subtract_bankroll(self, amount):
        
        self.bankroll -= amount

        
class Dealer(Person):
    
    def __init__(self):
        
        Person.__init__(self)
        
        
class Deck(object):
    
    def __init__(self):
        
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
        
    def deal_card(self):
        
        return self.cards.pop(randint(0,len(self.cards)-1))
    
    
player = Player()
dealer = Dealer()
    
while True:
        
    d = Deck()
        
    while True:
            
        try:
            
            print "You have %d chips" %(player.bankroll)
            bet = int(raw_input("How much would you like to bet? "))
            
        except:
            
            bet = int(raw_input("Invalid amount, how much would you like to bet? "))
        
        else:
            
            if (bet > player.bankroll):
                print "You don't have enough chips!"
            else:
                break
        
    player.get_card(d.deal_card())
    dealer.get_card(d.deal_card())
    player.get_card(d.deal_card())
    dealer.get_card(d.deal_card())
        
    print "Your cards are: %s" %(player.card_string())
    
    if (player.count_cards() != 21):
        
        while (raw_input("Do you want to hit? ")[0].lower() == 'y'):
            
            player.get_card(d.deal_card())
            print "Your cards are: %s" %(player.card_string())
            
            if (player.count_cards() >= 21):
                break
                
    if (player.count_cards() > 21):
        
        print "Sorry, you busted and lost the hand."
        player.subtract_bankroll(bet)
        
    elif (player.count_cards() == 21):
        
        print "You got 21, you win this hand!"
        player.add_bankroll(bet)
        
    else:
        
        while (dealer.count_cards() < 17):
            dealer.get_card(d.deal_card())
    
        print "The dealer's cards are: %s" %(dealer.card_string())
            
        if (dealer.count_cards() > 21):
            print "The dealer busted, you win this hand!"
            player.add_bankroll(bet)
        elif (player.count_cards() > dealer.count_cards()):
            print "You win this hand!"
            player.add_bankroll(bet)
        else:
            print "Sorry, the dealer wins this hand."
            player.subtract_bankroll(bet)
        
    if (player.bankroll == 0):
        
        print "You are out of chips! Game over..."
        break
        
    else:
        
        if (raw_input("Do you want to play another hand? ")[0].lower() == 'y'):
            player.clear_hand()
            dealer.clear_hand()
        else:
            break
        
        
    del d
    
