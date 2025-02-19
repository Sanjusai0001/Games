
#Roll_&_Dice

import random
import time

print("Welcome to Dice stimulator")
time.sleep(2)
print("Do you wanna play?")


def dice_game():

    x = "y"
    while x == "y":
        number = random.randint(1,6)

        if number == 1:
            print("----------")
            print("|        |")
            print("|   0   |")
            print("|        |")
            print("----------")
            break
        if number == 2:
            print("----------")
            print("|        |")
            print("|  0 0 |")
            print("|        |")
            print("----------")
            break
        if number == 3:
            print("----------")
            print("|    0   |")
            print("|    0   |")
            print("|    0   |")
            print("----------")
            break
        if number == 4:
            print("----------")
            print("| 0    0 |")
            print("|          |")
            print("| 0    0 |")
            print("----------")
            break
        if number == 5:
            print("----------")
            print("| 0    0 |")
            print("|    0    |")
            print("| 0    0 |")
            print("----------")
            break
        if number == 6:
            print("----------")
            print("| 0    0 |")
            print("| 0    0 |")
            print("| 0    0 |")
            print("----------")
            break

    x = input("press y to roll again")

# def Continue(dice_game):
#
#     if
#     dice_game()
dice_game()