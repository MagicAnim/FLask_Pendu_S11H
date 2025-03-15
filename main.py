# On importe la classe Flask du module flask
from flask import Flask, render_template, session, redirect
# On importe os
import os
# On import le module random
import random
# On crée une instance de Flask stocké dans la variable app
app = Flask("My Première App Web avec Flask")


# On définit notre clef secrète pour la création des cookies
app.secret_key = os.urandom(24)

# On définit notre route de page d'accueil
@app.route('/')
def initialisation():
    # On crée une liste de mots 
    liste_de_mots = ["magic", "souris", "dns","déni","application","router", "clavier","fonction","trace","ravin"]
    # On choisit aléatoirement un mot de cette liste
    mot_a_deviner = random.choice(liste_de_mots)
    vies = 6 
    print(mot_a_deviner)

    return "Test"





# Démarre le serveur Flask
# Host: "0.0.0.0" -> Configure Flask pour accepter des connexions provenant de toutes les adresses IP
# port = 81 : Définit le port sur lequel l'application sera accessible
app.run(host = '0.0.0.0', port = 81)