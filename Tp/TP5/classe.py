import math

#Exemple du cours
class Cylindre ():

    #Constructeur de Cylindre
    def __init__(self, rayon = 0, hauteur = 0, volume = 0): #self pour préciser qu'une méthode s'applique sur l'obojet basé sur la classe 
        self.__rayon = rayon
        self.__hauteur = hauteur
        self.volume = volume

    def setRayon(self,rayon):
        self.__rayon = rayon

    def setHauteur(self,hauteur):
        self.__hauteur = hauteur

    def calculerVolume(self):
        self.__volume = math.pi * self.__rayon * self.__rayon * self.__hauteur

    def getRayon(self):
        return self.__rayon
    
    def getHauteur(self):
        return self.__hauteur
    
    def getVolume(self):
        return self.__volume

#Programme Principal
#-------------------#

#Instanciation de l'objet cylindre1 :
print("Cylindre 1")

cylindre1 = Cylindre(15,5)

#Opérations sur l'objet cylindre1
print(cylindre1.getRayon())
print(cylindre1.getHauteur())
cylindre1.calculerVolume()
print(cylindre1.getVolume())


#Instanciation de l'objet cylindre2 :
cylindre2 = Cylindre()

#Opérations sur l'objet cylindre2
cylindre2.setRayon(4)
print(cylindre2.getRayon())
cylindre2.setHauteur(3)
print(cylindre2.getHauteur())
cylindre2.calculerVolume()
print(cylindre2.getVolume())
