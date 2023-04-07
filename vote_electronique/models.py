from django.db import models
from django.contrib.auth.models import User

class Election(models.Model):
    titre = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    biographie = models.TextField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

class Vote(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    date_vote = models.DateTimeField(auto_now_add=True)

