#Exercice 6

def get_odd_reverse(liste):
    liste_inverse = liste [::-1]
    new_liste = []
    for elem in liste_inverse:
        if elem %2 == 1:
            new_liste.append(elem)
    return new_liste

la_liste = [10,15,11,2,65,3,87,89]
out = get_odd_reverse(la_liste)
print(out)