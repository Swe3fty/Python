#Exercice 6 - Inversion de l'ordre des éléments d'une liste

def get_odd_reverse(input_list):
    list_impair = []
    for elem in input_list:
        if elem % 2 == 1:
            list_impair.append(elem)

    n = len(list_impair)
    for _ in range(n):  
        for i in range(n - 1):  
            if list_impair[i] < list_impair[i + 1]:  
                list_impair[i], list_impair[i + 1] = list_impair[i + 1], list_impair[i]

    return list_impair



input_list = [10, 15, 11, 2, 65, 3, 87, 89]
list_impair = get_odd_reverse(input_list)


for index in range(len(list_impair)):
    print(list_impair[index])
