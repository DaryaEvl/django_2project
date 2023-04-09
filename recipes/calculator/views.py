from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet(request):
    servings = int(request.GET.get("servings", 1))
    if servings == 1:
        print(DATA["omlet"])
        return HttpResponse(str(DATA["omlet"]))
    elif servings <= 0:
        return HttpResponse("Указано неверное количество")
    else:
        omlet_servings = {}
        for ingredient, quantity in DATA["omlet"].items():
            omlet_servings[f"{ingredient}"] = quantity * servings
        print(omlet_servings)
        return HttpResponse(str(omlet_servings))

def pasta(request):
    servings = int(request.GET.get("servings", 1))
    if servings == 1:
        return HttpResponse(str(DATA["pasta"]))
    elif servings <= 0:
        return HttpResponse("Указано неверное количество")
    else:
        pasta_servings = {}
        for ingredient, quantity in DATA["pasta"].items():
            pasta_servings[f"{ingredient}"] = quantity * servings
        return HttpResponse(str(pasta_servings))

def buter(request):
    servings = int(request.GET.get("servings", 1))
    if servings == 1:
        return HttpResponse(str(DATA["buter"]))
    elif servings <= 0:
        return HttpResponse("Указано неверное количество")
    else:
        buter_servings = {}
        for ingredient, quantity in DATA["buter"].items():
            buter_servings[f"{ingredient}"] = quantity * servings
        return HttpResponse(str(buter_servings))

