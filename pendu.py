# Importation de unicode pour retirer les accents
# Pour l'installation pip install unidecode
from unidecode import unidecode

# On crée notre classe Pendu
class Pendu:

    ####################################################
    #                 Les attributs                    #
    ####################################################
    # On crée les différents attributs qui vont nous permettent de suivre le jeu
    vies = 0
    mot_a_deviner = ""
    mot_a_afficher = ""
    # Une liste des lettres que l'utilisateur a déjà proposées
    lettres_proposees = []

    ####################################################
    #           1e Methode : INITIALISATION            #
    ####################################################
    # On crée une méthode pour initialiser le jeu
    def initialisation( vies , mot_a_deviner ):
        # On met en majuscule le mot à deviner
        mot_a_deviner = unidecode(mot_a_deviner).upper()
        # On affiche le mot à deviner
        print("Lors de cette partie le mot à deviner est ", mot_a_deviner)
        # On crée un dictionnaire qui va permettre de suivre l'état du jeu sur l'ensemble des pages etc
        data_etat_du_jeu = {
            "mot_a_deviner" : mot_a_deviner,    
            "mot_a_afficher" : "-" * len(mot_a_deviner),
            "lettres_proposees": [], # la liste de toutes les lettres que l'utilisateur a déjà proposées
            "vies" : vies,
            "victoire" : False,    # Passe à vrai si le joueur gagne
            "defaite" : False,
            "lettre_proposee": "" # La lettre proposée par le joueur
        }

        # On renvoie notre etat_du_jeu
        return(data_etat_du_jeu)


    ####################################################
    #           2e Methode : DEVINER                   #
    ####################################################

    # Methode principale qui va permettre de verifier l'input de l'utilisateur
    # On lui fourni les données du jeu et l'entrée de l'utilisateur

    def deviner( data_etat_du_jeu , entree):
        # On récupère toutes les variables de manière global
        global vies 
        global mot_a_deviner 
        global mot_a_afficher
        global lettres_proposees

        # On modifie les variables avec nos données temp
        vies = data_etat_du_jeu["vies"]
        mot_a_deviner = data_etat_du_jeu["mot_a_deviner"]
        mot_a_afficher = data_etat_du_jeu["mot_a_afficher"]
        lettres_proposees = data_etat_du_jeu["lettres_proposees"]

        # On crée les données renvoyées selon la proposition du joueur
        # Dictionnaire : * derniere_entree, victoire & defaite
        data_renvoyee = {
                "derniere_entree": entree,
                "victoire": False ,
                "defaite": False,
                "message": ""
        }
        if len(entree) == 1:
            message = Pendu.deviner_lettre(entree)
        else :
            message = Pendu.deviner_mot(entree)

        data_renvoyee["vies"] = vies
        data_renvoyee["mot_a_deviner"] = mot_a_deviner
        data_renvoyee["mot_a_afficher"]  = mot_a_afficher
        data_renvoyee["lettres_proposees"] = lettres_proposees
        data_renvoyee["message"] = message

        # On vérifie si le joueur perd avec le nombre de vies
        if vies == 0: 
             data_renvoyee["defaite"] = True

        # On vérifie si le joueur a  gagné
        if  data_renvoyee["mot_a_afficher"]  == data_renvoyee["mot_a_deviner"]: 
            data_renvoyee["victoire"] = True

        # On renvoie notre data_renvoyee pour informer l'application web de la victoire ou de la perte  du joueur
        return data_renvoyee




    ####################################################
    #        3e Methode : DEVINER  LETTRE              #
    ####################################################

    # On vérifie si la lettre appartient au mot et on l'ajoute aux lettres proposées
    def deviner_lettre(entree):
        # On récup nos variables 
        global vies 
        global mot_a_deviner 
        global lettres_proposees

        # On vérifie si la lettre n'a pas déjà été proposée sinon l'ajoute
        if entree in lettres_proposees:
            return "Tu as déjà proposé cette lettre ! Tentes-en une autre !"
        else:
            lettres_proposees.append(entree)

            # On vérifie si elle est dans le mot sinon on perd une vie
            if entree in mot_a_deviner :
                Pendu.actualisation_mot_a_afficher(entree)
                return "Bonne pioche !"
            else :
                vies -= 1
                return "Dommage ! Le mot ne contient pas '" + entree + "' ! " + " Tu n'as plus que " + str(vies) + " !"  



        ####################################################
        #           4e Methode : DEVINER  MOT              #
        ####################################################

        # On vérifie si le mot proposé est bien celui à deviner
    def deviner_mot(entree):
        global vies 
        global mot_a_deviner 
        global mot_a_afficher

            # Si c'est le cas on affiche le résultat + bravo autrement on enlève une vie
        if entree == mot_a_deviner :
                mot_a_afficher = entree
                return "Bravo, tu as gagné !"
        else :
                vies -= 1
                return "Dommage ! Ce n'est le mot '" + entree + "' ! " + " Tu n'as plus que " + str(vies) + " !"  


        ####################################################
        #   5e Methode :  Actualisation de mot_a_afficher   #
        ####################################################

        # On actualise le mot_a_afficher en rajoutant la lettre proposée
    def actualisation_mot_a_afficher(lettre_proposee):
        # On récup les variables dont on a besoin
        global mot_a_deviner 
        global mot_a_afficher
        # On parcourt mot_a_deviner avec notre itérateur i
        # Immuabilité des str donc on passe par les listes
        for i in range(len(mot_a_deviner)) :
            if lettre_proposee ==  mot_a_deviner[i]:
                    # On crée la liste mot = ["-","-","-","-","-"]   (exemple)
                    mot = list(mot_a_afficher)
                    # On ajoute la lettre à la bonne position : ["-","a","-","-","-"] (exemple)
                    mot[i] = lettre_proposee
                    # On recrée la str : "-a---" (exemple)
                    mot_a_afficher = ''.join(mot)

