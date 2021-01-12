import random

print("Guessing Game Guess A Number Between 1 to 9")

num = random.randint(1,9)

chances = 0

while chances < 5:
    inputNumber = int(input("Input A Number: "))
    
    if inputNumber == num:
        print("You Won")
        break
    elif inputNumber < num:
        print("Your number was too low")   
    else:
        print("Your number was too high")
    
    chances = chances + 1

if not chances < 5:
    print("You ran out of chances, number was ", num)    
