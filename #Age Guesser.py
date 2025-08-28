#Age Guesser
import random

def AgeGuesser():
    print("I'm going to guess your age!")
    name = input("What is your name? ")
    
    success = False
    while not success:
        guessed_age = random.randint(15,30)
        answer = input(f"Is your age {guessed_age} ? (y/n):")

        if answer == "y" or answer == "Y":
            print(name + f" is {guessed_age} years old.")
            success = True
            return True
        elif answer == 'n' or answer == 'N':
            print ("Rats!")

        else:
            print('Please say y or n.')


def main():
    AgeGuesser()
    return 0

main()
    