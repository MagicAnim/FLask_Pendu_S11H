# On importe la classe Flask du module flask
from flask import Flask, render_template, session, redirect
# On importe os
import os
# On crée une instance de Flask stocké dans la variable app
app = Flask("My Première App Web avec Flask")
# On importe les questions
from questions import questions
# On importe les resultats
from resultats import resultats

# On définit notre clef secrète pour la création des cookies
app.secret_key = os.urandom(24)





# Démarre le serveur Flask
# Host: "0.0.0.0" -> Configure Flask pour accepter des connexions provenant de toutes les adresses IP
# port = 81 : Définit le port sur lequel l'application sera accessible
app.run(host = '0.0.0.0', port = 81)