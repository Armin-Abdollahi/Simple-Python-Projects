#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def hangman():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    random_word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")

    while tries > 0:
        guessed_word = ""

        for letter in random_word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        if guessed_word == random_word:
            print("Congratulations! You won!")
            break

        print("Word: ", end="")
        for char in guessed_word:
            print(char, end=" ")
        print("\n")

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in random_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                tries -= 1
                print("Wrong guess! You have", tries, "tries left.")
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

    if tries == 0:
        print("Game over! The word was:", random_word)

hangman()

