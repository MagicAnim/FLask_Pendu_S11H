from unidecode import unidecode

# On crée notre classe Pendu pour la gestion complète du jeu
class Pendu:
    # On crée les attributs dont on a besoin pour le jeu
    vies = 0
    mot_a_deviner = ""
    mot_a_afficher = ""
    # On crée une liste pour stocker toutes les lettres que l'utilisateur a déjà proposées
    lettres_proposées = []

    ###########################################################
    #                1ere Méthode Initialisation              #
    ###########################################################
    def initialisation(mot_a_deviner, vies):
        # On gère les caractères spéciaux et on met toutes les lettres en majuscules
        mot_a_deviner = unidecode(mot_a_deviner).upper()

        data_etat_du_jeu = {
                "vies" : vies,
                "mot_a_deviner" : mot_a_deviner,
                "mot_a_afficher" : "-" * len(mot_a_deviner),
                "lettres_proposées": [],
                "victoire" : False,
                "defaite" : False,
                "entree" : ""
        }

        return data_etat_du_jeu