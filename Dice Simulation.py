#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def roll_dice():
    return random.randint(1,6)

def simulate_dice(num_rolls):
    results = []
    for _ in range(num_rolls):
        result = roll_dice()
        results.append(result)
    return results

num_rolls = int(input("Enter the number of dice rolls: "))
dice_results = simulate_dice(num_rolls)

print("The results of the dice roll:")
for result in dice_results:
    print(result)

