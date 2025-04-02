#==================Exercice 1======================

class CompteBancaire():
    #Constructeur
    def __init__(self,nom = "Martin",solde = 10000):
        self.__nom = nom
        self.__solde = solde

    def deposer (self,argent):
        self.__solde += argent
    
    def retirer (self,argent):
        self.__solde -= argent

    def afficher(self):
        print("Mr/Mme " + self.__nom + " votre solde de compte bancaire est de " + str(self.__solde))
    
compte1 = CompteBancaire("Duval", 1200)
compte1.deposer(125)
compte1.retirer(200)
compte1.afficher()

compte2 = CompteBancaire()
compte2.retirer(125)
compte2.afficher()