#Exercice 2 : Modulo qu'es aquò ?

total_secondes = int(input("Veuillez entrer un entier représentant un nombre de secondes\n"))

jours = total_secondes // 86400
reste_apres_jours = total_secondes % 86400

heures = reste_apres_jours // 3600
reste_apres_heures = total_secondes % 3600

minutes = reste_apres_heures //60
reste_total = reste_apres_heures % 60

print(f"{total_secondes} secondes sont équivalents à : {jours} jour(s), {heures} heure(s), {minutes} minute(s), {reste_total} seconde(s)")

