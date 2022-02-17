# Module schema permet de faire la validation et des réponses
from ninja import Schema
from datetime import datetime
from ninja.security import HttpBearer
from django.http import HttpRequest

# champs en entré
class PostInputSchema(Schema):
    title: str
    content:str

# Champs en sortie
class PostOutputSchema(Schema):
    id : int
    title : str
    content : str
    date_created : datetime

# Authentification : Authorization : Bearer : supersecret
class AuthBearer(HttpBearer):
    def authenticate(self, request:HttpRequest, token):
        if token == "supersecret":
            return token