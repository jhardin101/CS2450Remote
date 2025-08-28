#Age Guesser
import random

def AgeGuesser():
    print("I'm going to guess your age!")
    name = input("What is your name? ")
    guess_list = []
    
    success = False
    while not success:
        guessed_age = random.randint(15,30)
        while guessed_age in guess_list: 
            guessed_age = random.randint(15,30)

        answer = input(f"Is your age {guessed_age} ? (y/n):")
        guess_list.append(guessed_age)

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
    