#Cours Dictionnaire
#Exemple qu'on aurait utilisé de base
villes = ['Brest','Caen','Nantes']
temperatures = [15,17,12]
print(temperatures[1])

#Exemple de Dictionnaire
#Clés de type non mutables (list et dic ne marchent pas contre int, float, str ...)
#Valeurs de tous les types

dictionnaire = {"Brest":15,"Caen":17,"Nantes":12}
dictionnaire["Paris"] = 0.1
print(dictionnaire)
print(dictionnaire["Brest"])
print(dictionnaire["Paris"])

print(dictionnaire.keys())
print(dictionnaire.values())
print(dictionnaire.items())

#Création de boucles sur dictionnaire

dico = {"Oignon":2.1,"Navet":2.27,"Tomate":4.99}

for key in dico.keys():
    print(key)

for value in dico.values():
    print(value)

for key,value in dico.items():
    print(key,value)

#Les sets
s1 = {"apple",'orange',"apple","pear"}
s2 = {'orange','pear','cherry'}
print(s1|s2)
print(s1-s2)
print(s1&s2)

