from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_elections, name='liste_elections'),
    path('election/<int:election_id>/', views.details_election, name='details_election'),
    path('election/<int:election_id>/vote/', views.vote, name='vote'),
]

