# Score categories
# Change the values as you see fit
# поменять нахуй все return на присвоение к этим переменным 
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    d = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    for k in dice:
      d[k] += 1
    
    if category == ONES:
      return d[1]
    elif category == TWOS:
      return d[2] * 2
    elif category == THREES:
      return d[3] * 3
    elif category == FOURS:
      return d[4] * 4
    elif category == FIVES:
      return d[5] * 5
    elif category == SIXES:
      return d[6] * 6
    elif category == FULL_HOUSE:
      if 2 in d.values() and 3 in d.values():
        return sum(dice)
      else:
        return 0
    elif category == FOUR_OF_A_KIND:
      if 4 in d.values() or 5 in d.values() or 6 in d.values():
        for key in d:
          if d[key] >= 4:
            return key * 4
      else:
        return 0
    elif category == LITTLE_STRAIGHT:
      for i in range(1,6):
        if i in dice:
          continue
        else:
          return 0
      return 30
    elif category == BIG_STRAIGHT:
      for i in range(2,7):
        if i in dice:
          continue
        else:
          return 0
      return 30
    elif category == CHOICE:
      return sum(dice)
    elif category == YACHT:
      if len(set(dice)) == 1:
        return 50
      else:
        return 0
        
      
      
    
    
