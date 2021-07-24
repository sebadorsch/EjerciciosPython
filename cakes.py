"""def cakes(recipe, available):
    cantidad = 99999
    for elemento in recipe:
        if available.get(elemento):
            if available.get(elemento) // recipe.get(elemento) < cantidad:
                cantidad = available.get(elemento) // recipe.get(elemento)
        else:
            return 0
    return cantidad
"""

def cakes(recipe, available):
    return min(available.get(k, 0) // recipe[k] for k in recipe)


if __name__ == '__main__':
    # must return 2
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available), 2, 'example #1')