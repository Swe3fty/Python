#============Obtenir la liste des communes d'un département================
def get_communes_departement(initial_file_path, num_dep, length):
    file_handle = open(initial_file_path, "r")

    # Crée une liste avec les lignes du fichier, splitlines() permet de supprimer les \n et de convertir une chaine en liste
    list_lines = file_handle.read().splitlines() 
    list_communes = []
    for line in list_lines:
        string_left = line.split(";")[0]
        string_right = line.split(";")[1]
        if len(string_left) == length and string_right.startswith(str(num_dep)):
                list_communes.append(string_left)
    file_handle.close()
    return list_communes
    
#=============Ecrire le nom des communes dans un fichier================
def write_communes_departement(list_communes, final_file_path):
    file_handle = open(final_file_path, "w")
    for commune in list_communes:
        file_handle.write(commune + "\n")
    file_handle.close()



#==================Programme Principal====================
initial_file = "fichierCommunesBretagne.txt"
final_file = "fichierFinal.txt"

sorted_communes_list = get_communes_departement(initial_file, 29, 9)
write_communes_departement(sorted_communes_list, final_file)


    

