#==================Ouverture====================
file_handle = open("fichierCommunesBretagne.txt", "r")

#==================Lecture====================

#Crée une liste avec les lignes du fichier

#list_lines = file_handle.readlines()
#print(list_lines)

#Crée un extrait du contenu du fichier sous forme de chaine de charactères
text_lines = file_handle.read()
print(text_lines[:100])

#==================Fermeture====================
file_handle.close()