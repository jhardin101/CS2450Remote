#Age Guesser
import random

def AgeGuesser():
    print("I'm going to guess your age!")
    name = input("What is your name? ")
    guessed_age = random.randint(15,30)
    answer = input(f"Is your age {guessed_age} ?")
    success = False
    while not success:
        if answer == "Y" or "y":
            print(name + f" is {guessed_age} years old.")
            success = True
        else:
            print ("Rats!")
    return 0

def main():
    AgeGuesser()
    return 0

if "name" == '__main__':
    main()
    