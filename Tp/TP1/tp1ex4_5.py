#Exercice 4 - Diviseurs d'un nombre

def get_dividers (number):
    list = []
    for index in range(1,99,1):
        if number % index == 0:
            list.append(index)
    return list

def get_string(number):
    diviseurs = get_dividers(number)
    print(f"Le nombre {number} possède {len(diviseurs)} diviseur(s) qui est/sont le(s) suivant(s) : {diviseurs}" )

def get_advanced_string(number):
    diviseurs = get_dividers(number)
    if len(diviseurs) > 1:
        numbers = ", ".join(str(elem) for elem in diviseurs[:-1]) + " et " + str(diviseurs[-1])
    else:
        numbers = str(diviseurs[0])
    print(f"n = {number} possède {len(diviseurs)} diviseur(s): {numbers}" )

get_string(95)
get_string(99)
get_advanced_string(7)
get_advanced_string(4)
get_advanced_string(14)