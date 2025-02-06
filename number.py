import random

def rnumber():
    return random.randint(1,100)

select_number = rnumber()
print(select_number)
Tries = 0


def numbertrue(Guess):
    
    while not Guess == select_number:
        if Guess >= select_number:
            print(f"{Guess}is larger than the number!")
            Tries = Tries + 1
            Guess = int(input("Guess again!"))
        elif Guess <= select_number:
            print(f"{Guess} is smaller than the number!")
            Tries = Tries + 1
            Guess = int(input("Guess again!"))
    if Guess == select_number:
           return Guess
        

Guess = input("guess a number!")
Final_Guess = numbertrue(int(Guess))

print(f"{Final_Guess} is the right number! You used {Tries} tries!")