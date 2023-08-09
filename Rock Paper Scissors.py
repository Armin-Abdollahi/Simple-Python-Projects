#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ")
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock/paper/scissors): ")
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie🙂"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win😎"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("---------------------------------")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")
    
    result = determine_winner(user_choice, computer_choice)
    
    print(result)

play_game()

