import random
from collections import Counter
# Counter is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
import numpy as np

#Use numpy to generate the sides of the dice
sides = np.arange((1/6), (1), (1/6),dtype= float)*6

roll = np.round(sides).tolist()

#Create empty list to store our outcomes of the rolled dice

results=[]

#Ask user to select the number of times he/she wants the dice roll to ocurr.
val = int(input("Enter number of times you want to roll dice: "))
for i in range(val):
    outcome = random.choice(roll)
    results.append(outcome)

#Use collections counter to take frequency of our outcomes and store to a dictionary.
tally= Counter(results)
sort_dict= dict(sorted(tally.items()))

#Print our outcomes in a table. (Record the outcomes in a neat way)
print('FACE','   FREQUENCY',' PERCENTAGE(S)')
print('')
print('#################################')
for key, value in sort_dict.items():
    percentage = ((value/val)*100)
    percentage = str(round(percentage, 2))
    print('{:<10} {:<7} {:<1}'.format(key, value, str(percentage)+"%"))

totals= sum(sort_dict.values())
total_P= (totals/val)*100
print('')
print('#################################')
print('Total=   ',totals,'  '  , total_P,'%')
