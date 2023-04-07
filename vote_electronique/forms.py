from django import forms
from .models import Election, Candidat, Vote

class ElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = ['titre', 'date_debut', 'date_fin']

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ['nom', 'biographie', 'election']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['utilisateur', 'election', 'candidat']

