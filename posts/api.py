from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from django.http import HttpRequest
from .models import Post # Importation du modeles post
from .schemas import PostInputSchema,PostOutputSchema # Importation du schema
from django.shortcuts import get_list_or_404
from typing import List
from ninja.security import django_auth

api=NinjaAPI(csrf=True) # Objet principale

# Authentification : Enpoint
@api.get("/bearer", auth=django_auth)
def auth(request:HttpRequest):
    return {"token": request.auth}

# Endpoint : Create / ** : reçevoir les données du paramètres
@api.post('/post',response={201:PostOutputSchema})
def create_post(request:HttpRequest,payload:PostInputSchema):
    """
        Les informations pour éffectuer une insertion :
        - Title : Mettre un titre
        - Content : Mettre un contenu du titre
    """
    new_post=Post.objects.create(**payload.dict()) # Insertion dans la bd en objet

    return 201, new_post # Affichage du message du code 201

# Endpoint : get all 
@api.get('/posts',response=List[PostOutputSchema])
def get_all_posts(request:HttpRequest):
    all_posts=Post.objects.all() # Requete pour afficher tout les postes

    return all_posts  # Affichage 


# Endpoint : get one post
@api.get('/post/{post_id}',response={200:PostOutputSchema})
def get_an_post(request:HttpRequest,post_id:int):
    post=get_object_or_404(Post,pk=post_id) # Affchage erreur 404

    return 200, post


# Endpoint : update post
@api.put('/post/{post_id}',response={200:PostOutputSchema})
def update_post(request:HttpRequest,post_id:int,payload:PostInputSchema ):
    post_to_upadte=get_object_or_404(Post,pk=post_id) # Affchage erreur 404
    for attr, value in payload.dict().items():
        setattr(post_to_upadte, attr, value)
    # Modification des infos
    #post_to_upadte.title = payload.title        
    #post_to_upadte.content = payload.content

    post_to_upadte.save() # Modification

    return 200,post_to_upadte


# Endpoint : delete post
@api.delete('/post/{post_id}',response={204:None})
def delete_post(request:HttpRequest,post_id:int):
    post_to_delete=get_object_or_404(Post,pk=post_id)

    post_to_delete.delete() # Supprimer 

    return 204, None



