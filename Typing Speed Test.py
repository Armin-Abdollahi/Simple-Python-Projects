#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

def typing_speed_test():
    sentence = "The quick brown fox jumps over the lazy dog."
    print("Type this sentence as fast as you can:")
    print(sentence)
    print("-------------------------------------------------\n")
    input("Press Enter when you are ready to start.")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    total_time = end_time - start_time
    words_typed = len(user_input.split())
    
    speed = words_typed / total_time * 60
    
    print("\n-------------------------------------------------")
    print("Total time:", round(total_time, 2), "seconds")
    print("Your typing speed is", round(speed, 2), "words per minute.")

typing_speed_test()

