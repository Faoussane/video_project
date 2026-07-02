from django.db import models
from django.contrib.auth.models import AbstractUser
"""Créer une petite application où :

un utilisateur crée un compte
il se connecte
il peut enregistrer une vidéo
il ajoute un titre
une description
la date est enregistrée automatiquement
seul l'auteur peut modifier ou supprimer sa vidéo
tout le monde peut voir la liste des vidéos.
    """
class Utilisateur(AbstractUser):
    photo_url = models.ImageField(upload_to='profile/', blank=True)
    def __str__(self):
        return f'{self.username} - {self.email}'
class Video:
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return f'{str(self.titre).capitalize()} par {str(self.auteur).capitalize()}'
