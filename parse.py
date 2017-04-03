# read txt file
def parse():
    with open('recipes.txt', 'rU') as f:
        # read recipes in as a string
        lines = f.read()
    # split txt file into recipes
    s = lines.split('\n\n\n\n')
    # store as a python dictionary with a name, category, website, serving,
    # and ingredients
    recipes = []
    for recipe in s:
        d = {}
        lines = recipe.split('\n')
        d['name'] = lines[0]
        d['link'] = lines[1]
        d['category'] = lines[2]
        d['serving'] = lines[3]

        ingredients = []

        for ingredient in lines[4:]:
            i = {}
            x = ingredient.split(' ', 2)
            #{name: 'stuff', amount: 1.5, unit:"cups"}
            if len(x) == 3:
                i['amount'] = float(x[0])
                i['unit'] = x[1]
                i['name'] = x[2]

                ingredients.append(i)

        d['ingredients'] = ingredients

        recipes.append(d)

    # return list of recipes
    return sorted(recipes, key=get_sort_key)


def get_sort_key(recipe):
    return recipe['category']

if __name__ == '__main__':
    print parse()
