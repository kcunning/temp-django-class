from django.shortcuts import render, HttpResponse

from recipes.models import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 
        'recipelist.html', 
        {'recipelist': recipes})
        
def recipe_single(request, **kwargs):
    recipe = Recipe.objects.get(pk=kwargs['pk'])
    return render(request, 
        'recipesingle.html', 
        {'recipe': recipe})

