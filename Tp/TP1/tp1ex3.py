#Exercice 3 - Maximum dans une liste de nombres

#version 1
def my_maximum(list,length):
    compteur = 0
    maximum = list[0]
    while compteur < length:
        if maximum < list[compteur] :
            maximum = list[compteur]
            iterator = compteur
        compteur += 1
    return [maximum, iterator]




#version 2

def my_maximum2(list,length):
    number = list[0]
    counter = 0
    iterator = 0
    for num in list :
        if num > number :
            number = num
            iterator = counter
        counter += 1
    return [number, iterator]

#version 3

def my_maximum3(list,length):
    max = list[0]
    iterator = 0
    for counter in range(len(list)):
        if max < list[counter]:
            max = list[counter]
            iterator = counter 
    return [max,iterator]


list = [1,3,10,9]
max, iterator = my_maximum(list,len(list))
print(max, iterator)

max, iterator = my_maximum2(list,len(list))
print(my_maximum2(list,len(list)))

max, iterator = my_maximum2(list,len(list))
print(my_maximum3(list,len(list)))