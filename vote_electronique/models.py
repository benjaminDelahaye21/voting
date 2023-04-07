from django.db import models
from django.contrib.auth.models import User

class Electeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)

class Election(models.Model):
    titre = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    candidats = models.ManyToManyField('Candidat')

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

class Vote(models.Model):
    electeur = models.ForeignKey(Electeur, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    date_heure = models.DateTimeField(auto_now_add=True)

