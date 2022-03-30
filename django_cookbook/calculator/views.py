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


def home_view(request):
    msg = 'CookBook project'
    return HttpResponse(msg)


def recipe_view(request, dish):
    template_name = 'index.html'
    servings = int(request.GET.get('servings', 1))

    recipe = {}
    for ingridient, amount in DATA.get(dish).items():
        recipe[ingridient] = round(amount * servings, 2)

    context = {
        'recipe': recipe
    }

    return render(request, template_name, context)
