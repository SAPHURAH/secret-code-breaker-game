#Add a game menu

import random

print("Welcome to the Secrete Code Breaker!")

name = input("Enter your name:  ")

print(f"Hello {name} , let's see if you can crack the secrett code!")

print("Choose your diffuclty;Easy(1-10), Medium(1-50),  Hard(1-100)")

difficulty = input("Enter a difficulty: ").lower()

if difficulty == "easy":
    max_number = 10
elif difficulty == "medium":
    max_number = 50
else:
    max_number = 100

    
random_secret_code = random.randint(1, max_number)


attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < random_secret_code:
        print("Too low! Try again.")
    elif guess > random_secret_code:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congrats {name}! You cracked the code in {attempts} attempts.")
        break


while True:
   play_again = input("Do you want to play again? (yes/no): ").lower()
   if play_again != "yes":
         print("Thanks for playing! Bye!")
         break


