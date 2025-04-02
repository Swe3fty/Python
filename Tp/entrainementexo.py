

def my_maximum3(list):
    maximum = list[0]
    iterator
    for number in list:
        if maximum < number:
            maximum = number
            iterator = list[number]
    return maximum, iterator

list = [24, 46, 2, 67]
maximum, iterator = my_maximum3(list)
print(maximum, iterator)

