import random

class Card(object):  
    
    def __init__(self, color, suit):
        self.color = color 
        self.suit = suit
        
    def __repr__(self):
        return "{}{}".format(self.color, self.suit)

    def value(self, total):
        try: 
            return int(self.suit)
        except ValueError: 
            if self.suit == "J":
                return 10
            if self.suit == "Q":
                return 10
            if self.suit == "K":
                return 10
            if self.suit == "A":
                if total + 10 > 21:
                    return 1
                else: 
                    return 10


def make_deck():
    deck = []
    colors = ['♣','♦','♥','♠']
    for color in colors:
        for i in range(2,10):
            deck.append(Card(color,str(i)))
        deck.append(Card(color,'J'))
        deck.append(Card(color,'Q'))
        deck.append(Card(color,'K'))
        deck.append(Card(color,'A'))

    random.shuffle(deck)
    return deck


def main():
    deck = make_deck()
    print(deck)
    
    total = 0
    has_lost = False 
    wants_another = True
    while wants_another and not has_lost:
        card = deck.pop()
        print("You drew {}.".format(card))
        total += card.value(total)
        print("sum: {}".format(total))
        if total == 21:
            print("You win.")
            return 
        elif total > 21:
            print("You lose.")
            has_lost = True
        else: 
            choice = input("Do you want another card? (y/n)")
            while choice not in ['y','n']:
                print("Invalid input.")
                input("Do you want another card? (y/n)")
            if choice == 'n':
               wants_another = False 
            
    if not has_lost: 
        print("My turn.")
        dealer_total = 0
        while dealer_total < 17:
            card = deck.pop()
            print("I drew {}".format(card))
            dealer_total += card.value(dealer_total)
            print("My sum: {}".format(dealer_total))
        if dealer_total == 21: 
            print("I win.")
        elif dealer_total > 21: 
            print("You win.")
        elif dealer_total == total: 
            print("Push")
        elif dealer_total > total:
            print("I win.")
        else: 
            print("You win.")

if __name__ == "__main__":
    main()