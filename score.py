from __future__ import division # default to floating point division
from cards import hearthstoneCards as cards
import math

TYPE_CREATURE = 4 
TYPE_SPELL = 5
TYPE_WEAPON = 7

CLASS_WARRIOR = 1
CLASS_PALADIN = 2
CLASS_HUNTER = 3
CLASS_ROGUE = 4
CLASS_PRIEST = 5
CLASS_SHAMAN = 7
CLASS_MAGE = 8
CLASS_WARLOCK = 9
CLASS_DRUID = 11

CLASS_NAME = {1 : "Warrior",
              2 : "Paladin",
              3 : "Hunter",
              4 : "Rogue",
              5 : "Priest",
              7 : "Shaman",
              8 : "Mage",
              9 : "Warlock",
              11 : "Druid"}

ALL_CLASSES = [CLASS_WARRIOR, CLASS_PALADIN, CLASS_HUNTER,
               CLASS_ROGUE, CLASS_PRIEST, CLASS_SHAMAN,
               CLASS_MAGE, CLASS_WARLOCK, CLASS_DRUID]

# values from curi's TL post
VALUE_ATTACK = 1
VALUE_HEALTH = 1
VALUE_TAUNT = 1
VALUE_CHARGE = 3
VALUE_DIVINE_SHIELD = 3
VALUE_BATTLECRY_DAMAGE = 2.5
VALUE_SPELL_DAMAGE = 1
VALUE_CARD_DRAW = 3

# speculative values
VALUE_CANT_ATTACK = -4
VALUE_OVERLOAD = -1 

# value a card
def value(c):
    actual = 0
    budget = 1 + c["cost"] * 2
    base = 0
    desc = 0

    if "attack" in c:
        base += VALUE_ATTACK * c["attack"]

    if "health" in c:
        base += VALUE_HEALTH * c["health"]
    
    
    
    if "description" in c:
        accounted_for = True
        if c["description"] == "Taunt":
            desc += VALUE_TAUNT
        elif c["description"] == "Charge":
            desc += VALUE_CHARGE
        elif c["description"] == "Divine Shield":
            desc += VALUE_DIVINE_SHIELD
        elif c["description"] == "Battlecry: Deal 1 damage.":
            desc += VALUE_BATTLECRY_DAMAGE
        elif c["description"] == "Battlecry: Deal 2 damage.":
            desc += VALUE_BATTLECRY_DAMAGE * 2
        elif c["description"] == "Battlecry: Deal 3 damage.":
            desc += VALUE_BATTLECRY_DAMAGE * 3
        elif c["description"] == "Spell Damage +1":
            desc += VALUE_SPELL_DAMAGE
        elif c["description"] == "Spell Damage +5":
            desc += VALUE_SPELL_DAMAGE*5
        elif c["description"] == "Battlecry: Deal 4 damage to HIMSELF.":
            desc -= VALUE_HEALTH * 4
        elif c["description"] == "Can't Attack.":
            desc += VALUE_CANT_ATTACK
        elif c["description"] == "Whenever this minion takes damage, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Whenever you cast a spell, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Choose a minion.  Whenever it attacks, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Whenever one of your other minions dies, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Whenever you summon a Beast, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "At the end of your turn, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "At the end of your turn, you have a 50% chance to draw a card.":
            desc += 0.5 * VALUE_CARD_DRAW
        elif c["description"] == "Whenever a minion is healed, draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Battlecry: Draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Deathrattle: Draw a card.":
            desc += VALUE_CARD_DRAW
        elif c["description"] == "Spell Damage +1. Battlecry: Draw a card.":
            desc += VALUE_CARD_DRAW
            desc += VALUE_SPELL_DAMAGE
        elif c["description"] == "Spell Damage +1. Deathrattle: Draw a card.":
            desc += VALUE_CARD_DRAW
            desc += VALUE_SPELL_DAMAGE
        elif c["description"] == "Draw 2 cards.":
            desc += VALUE_CARD_DRAW * 2
        elif c["description"] == "Draw 4 cards.":
            desc += VALUE_CARD_DRAW * 4
        elif c["description"] == "Taunt. Overload: (3)":
            desc += VALUE_TAUNT
            desc += VALUE_OVERLOAD*3
        else:
            print "Not sure how to value", c["description"]

    actual = base+desc
    return actual-budget, budget, actual, base, desc, c

everything = []

for c in cards:
    everything += [value(c)]

sorted_everything = sorted(everything, reverse=True)


print "over", "\t", "budget", "\t", "actual", "\t",
print "base", "\t", "desc", "\t", "card", "\t",
print "description"
for c in sorted_everything:
    print c[0], "\t", c[1], "\t", c[2], "\t",
    print c[3], "\t",
    if c[4] == 0:
        print "@",
    else:
        print c[4],
    print "\t",
    print c[5]["name"],
    if "description" in c[5]:
        print "\t", c[5]["description"]
    else:
        print

