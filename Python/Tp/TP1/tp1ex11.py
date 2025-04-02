#Exercice 11

for counter in range (9,0,-1):
    print("*"*counter)

for counter in range(9,0,-1):
    chaine=""
    for counter2 in range(counter):
        chaine +="*"
    print(chaine)