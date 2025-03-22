# On importe la classe Flask du module flask
from flask import Flask, render_template, session, redirect, request
# On importe os
import os
# On import le module random
import random
# On importe notre classe Pendu de notre ficher pendu.py
from pendu import Pendu
# On crée une instance de Flask stocké dans la variable app
app = Flask("Jeu du Pendu")


# On définit notre clef secrète pour la création des cookies
app.secret_key = os.urandom(24)

# On définit notre route de page d'accueil
@app.route('/')
def initialisation():
    # On crée une liste de mots 
    liste_de_mots = ["magic", "souris", "dns","déni","application","router", "clavier","fonction","trace","ravin"]
    # On choisit aléatoirement un mot de cette liste
    mot_a_deviner = random.choice(liste_de_mots)
    # On définit le nombre de vies
    vies = 6 
    # On initialise le jeu
    session["etat_du_jeu"] = Pendu.initialisation(vies, mot_a_deviner)
    # On redirige vers l'affichage de notre jeu
    return redirect("/jeu")

# On définit un route pour l'affichage
@app.route("/jeu")
def affiche():
    return render_template("pendu.html", etat_du_jeu = session["etat_du_jeu"])


# On définit le route pour deviner = actualiser avec l'entrée de l'utilisateur
@app.route("/deviner", methods=["POST"])
def deviner():
    # Récupération de l'entrée du formulaire
    entree = request.form["entree"]
    # On update le jeu avec la méthode deviner qui permet de vérifier l'entrée de l'utilisateur et de raffraichir le jeu
    session["etat_du_jeu"] = Pendu.deviner(session["etat_du_jeu"], entree)
    # On affiche le jeu de nouveau
    return redirect("/jeu")

# Démarre le serveur Flask
# Host: "0.0.0.0" -> Configure Flask pour accepter des connexions provenant de toutes les adresses IP
# port = 81 : Définit le port sur lequel l'application sera accessible
app.run(host = '0.0.0.0', port = 81)