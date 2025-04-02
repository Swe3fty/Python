#Exemple de boucle for sur une liste
#for sans range

liste =[4,'Brest','U',47.2,True]
for elem in liste[2:4]: #start(inclus) stop : Exclu
    print(elem)



#for avec range
for counter in range (2,4): #start(inclues) stop : Exclu
    print(liste[counter])


#autre exemple
var1 = [42,24,17,2,1]
print(var1[1])
print(var1[0:3])
print(var1[:3]) #début à 3
print(var1[3:]) #début à 3 fin
print(var1[:3:2]) # 42,17 - start -stop - step
print(var1[len(var1)-1]) # 1
print(var1[-1]) #1

#: signifie opérateur de slicing