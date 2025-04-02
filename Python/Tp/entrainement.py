variable = "13"
print(type(variable))
if not variable.isalpha() :
    print("ce n'est pas une chaine de charactère contenant une lettre")

compteur = 5
while compteur > 0:
    print("oui")
    compteur -= 1


for index in range(0,5,1):
    print(index)

for elem in ["Isen", 13.3, 14]:
    print(elem)

chaine = "Bonsoir?Bonjour"
print(chaine.replace("?","!"))
print(chaine.split("?"))
for index in chaine:
    print('->' + index)

chaine = "Isen"
print(chaine[::2])