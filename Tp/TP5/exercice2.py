#==================Exerice 2=====================
#Crée une classe MyString qui permet d'effectuer des opérations spécifiques sur des chaînes de caractères

class MyString ():

    #Constructeur
    def __init__(self, chaine = ""):
        self.__chaine = chaine
        self.__nombreVoyelles = 0
        self.__nombreConsonnes = 0

    def updateNumberLetters(self):
        capitalized = self.__chaine.upper()
        numVoy = 0
        numCon = 0
        for letter in capitalized:
            if letter in ['A','E','I','O','U','Y']:
                numVoy += 1
            else :
                numCon += 1
        self.__nombreVoyelles = numVoy
        self.__nombreConsonnes = numCon

    def getSentence(self):
        return self.__chaine

    def getNumberVoyelles(self):
        return self.__nombreVoyelles
    
    def getNumberConsonnes(self):
        return self.__nombreConsonnes
    
    def affichageNombres(self):
        print("La chaîne de charactères '" + self.__chaine + ".' comporte " +self.__nombreVoyelles + " voyelle(s) et " + self.__nombreConsonnes + "consonnes" )

    def setSentence(self, str):
        self.__chaine == str
        
chaine1 = MyString("bonjour")
chaine1.updateNumberLetters()
print(chaine1.getNumberConsonnes())
print(chaine1.getNumberVoyelles())
#erreur print(chaine1.__chaine)

