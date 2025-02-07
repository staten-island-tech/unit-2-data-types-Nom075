import random

def rnumber():
    return random.randint(1,100)

select_number = rnumber()
Tries = 0


def numbertrue(Guess):
    Tries = 0
    while not Guess == select_number:
        if Guess >= select_number:
            print(f"{Guess} is larger than the number!")
            Tries = Tries + 1
            Guess = int(input("Guess again!"))
        elif Guess <= select_number:
            print(f"{Guess} is smaller than the number!")
            Tries = Tries + 1
            Guess = int(input("Guess again!"))
    if Guess == select_number:
           Tries = Tries + 1
           return Guess, Tries
        

Guess = input("guess a number!")
Final_Guess, Final_Tries = numbertrue(int(Guess, Tries))

print(f"{Final_Guess} is the right number! You used {Final_Tries} tries!")