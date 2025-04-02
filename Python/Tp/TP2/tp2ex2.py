#Exercice 2 - Scrabble

def calculer_score(mot, points_lettres):
    score = 0
    for lettre in mot:
        for points, lettres in points_lettres.items():
            if lettre in lettres:
                score += points
    return score

def calculer_score1(mot, points_lettres):
    score = 0
    for lettre in mot:
        for points in points_lettres:
            if lettre in points_lettres[points]:
                somme_points += points
    return somme_points
    


points_lettres = {
    1 : ["E","A","I","N","O","R","S","T","U","L"],
    2 : ["D","M","G"],
    3 : ["B","C","P"],
    4 : ["F", "H", "V"],
    8 : ["J", "Q"],
    10 : ["K", "W","X","Y","Z"]
}


print(calculer_score("POMME", points_lettres))
print(calculer_score("JUXEBOX", points_lettres))

#print ("cou" in "coucou")