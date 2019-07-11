#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[3]:


def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled


# In[4]:


def main():
    sides =6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? Enter= Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling = False
    print("Thanks for playing.")
    
main()


# In[ ]:




