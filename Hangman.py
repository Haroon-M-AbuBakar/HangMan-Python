import random
import string
import time
from word import words

word = random.choice(words)
word = word.upper()


word_letters = set(word)
correctly_guessed_letters = set()
english_letters = set(string.ascii_uppercase)

attempts = 7

while correctly_guessed_letters != word_letters:

    print("Attempts Remaining : " + str(attempts))
    dash_on_letter = [letter if letter in correctly_guessed_letters else '?' for letter in word]
    print(dash_on_letter)
    user_letters = input("Enter a guess : ").upper()

    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]

    match attempts:

        case 1:
            print(stages[0])

        case 2:
            print(stages[1])

        case 3:
            print(stages[2])

        case 4:
            print(stages[3])

        case 5:
            print(stages[4])

        case 6:
            print(stages[5])

        case 7:
            print(stages[6])



    if user_letters in word_letters:
        print("Correct Guess")
        correctly_guessed_letters.add(user_letters)

    elif user_letters in english_letters - word_letters:
        print("Try again")
        attempts = attempts - 1



if correctly_guessed_letters == word_letters:
    print("You won,The word was : " + str(word))