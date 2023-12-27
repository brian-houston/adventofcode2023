import functools
hand_order = {
        (1,1): 0,
        (2,1): 1,
        (2,2): 2,
        (3,1): 3,
        (3,2): 4,
        (4,1): 5,
        (5,): 6,
        }

card_order = {
        '2': 0,
        '3': 1,
        '4': 2, 
        '5': 3, 
        '6': 4, 
        '7': 5, 
        '8': 6, 
        '9': 7, 
        'T': 8, 
        'J': 9,
        'Q': 10,
        'K': 11,
        'A': 12
        }

ncards = 13

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        counts = {}  
        for c in cards:
            counts.setdefault(c, 0)
            counts[c] += 1
        counts = counts.values()
        counts = sorted(counts, reverse = True)
        self.type = hand_order[tuple(counts[:2])]

    def __repr__(self):
        return self.cards 

def cmp_hands(a,b):
    if a.type != b.type:
        return a.type - b.type
    for i in range(5):
        av = card_order[a.cards[i]]
        bv = card_order[b.cards[i]]
        if av != bv:
            return av - bv 

lines = open('inputs/day7', 'r').read().split('\n') 
hands = [Hand(*x.split()) for x in lines if x]
hands.sort(key = functools.cmp_to_key(cmp_hands))
hands = [i * h.bid for i, h in enumerate(hands, 1)]
print(sum(hands))
