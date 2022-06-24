"""

<a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
___
<center><em>Content Copyright by Pierian Data</em></center>

# Guessing Game Challenge

Let's use `while` loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is
 * within 10 of the number, return "WARM!"
 * further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is 
 * closer to the number than the previous guess return "WARMER!"
 * farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!


#### First, pick a random integer from 1 to 100 using the random module and assign it to a variable

#Note: `random.randint(a,b)` returns a random integer in range `[a, b]`, including both end points.
"""
from random import randint
random_number = randint(1, 100)

random_number

liste = []

print("""HELLOOOO EVERYONE!
It is a prediction of number game and number range is between 1 and 100
If your guess is more than 10 away from my number, I'll tell you you're COLD
If your guess is within 10 of my number, I'll tell you you're WARM
If your guess is farther than your most recent guess, I'll say you're getting COLDER
If your guess is closer than your most recent guess, I'll say you're getting WARMER
LETS START!""")

while True:
    a = int(input("Lets enter the prediction?: ")) 
    liste.append(a)
    if a<1 or a>100:
        print("OUT OF BOUNDS")
    elif abs(a-random_number)<=10:
        print("WARM!")
    elif abs(a-random_number)>10:
        print("COLD!")
    if len(liste)>1:
        if abs(liste[-1]-random_number)>abs(liste[-2]-random_number):
            print("COLDER!")
        else:
            print("WARMER!")
    if a==random_number:
        print(f"""YAAAY! You've correctly guessed the number {random_number}! 
                If you ask how many guesses it took? It took {len(liste)} times!""")
        break
        
    
