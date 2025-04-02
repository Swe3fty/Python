#Exercice 1 : Nombres pairs et impairs

#fonction
def parite(nombre):
    if nombre % 2 == 0 :
        print("Le nombre entré est pair")
    elif nombre % 2  == 1 :  
        print("Le nombre entré est impair") 

#main
while 1 :
    nombre = input("Entrez un nombre pour vérifier sa parité, -1 pour arreter\n")
    if int(nombre) == -1 :
     exit()
    else :    
        parite(int(nombre))
#++ et -- ne marchent pas en python
