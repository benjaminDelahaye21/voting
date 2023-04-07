from django.shortcuts import render, redirect
from .models import Election, Candidat, Vote
from .forms import ElectionForm, CandidatForm, VoteForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def liste_elections(request):
    elections = Election.objects.all()
    return render(request, 'vote_electronique/liste_elections.html', {'elections': elections})

def details_election(request, election_id):
    election = Election.objects.get(pk=election_id)
    candidats = Candidat.objects.filter(election=election)
    return render(request, 'vote_electronique/details_election.html', {'election': election, 'candidats': candidats})

def vote(request, election_id):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.utilisateur = request.user
            vote.election_id = election_id
            vote.save()
            return redirect('liste_elections')
    else:
        form = VoteForm()
    return render(request, 'vote_electronique/vote.html', {'form': form})

def inscription(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accueil")
    else:
        form = UserCreationForm()
    return render(request, "inscription.html", {"form": form})

def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("accueil")
    else:
        form = AuthenticationForm()
    return render(request, "connexion.html", {"form": form})

def deconnexion(request):
    logout(request)
    return redirect("connexion")

def accueil(request):
    return render(request, "accueil.html")
# Create your views here.
