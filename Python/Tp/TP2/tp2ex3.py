#Exercice 421
import random

def display_dices(list_dices):
    print(f"Dé 1 {list_dices[0]} ; Dé 2 : {list_dices[1]} ; Dé 3 : {list_dices[2]}")

def input_and_convert(my_string):
    nombre = int(input(my_string))
    return nombre

def get_dices_values():
    list_dices = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    return list_dices

def redraw_dice(list_dice, num_dice):
    list_dice[num_dice] = random.randint(1,6)

def game_rules(list_dices):
    for index in range(len(list_dices)):
        if list_dices[index] == list_dices[index+1] or list_dices[index] == list_dices[index+2] or list_dices[index+1] == list_dices[index+2]:
            print("Vous avez gagné")

