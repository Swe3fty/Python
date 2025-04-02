#Exercice 7 - Note moyenne

def get_average(list):
    moyenne = 0
    for elem in list:
        moyenne += elem
    return moyenne/len(list)

list = [12,13,14]
moyenne = get_average(list)
print(moyenne)