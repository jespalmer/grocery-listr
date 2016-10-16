from parse import parse


def print_recipes():
    recipes = sorted(parse(), key=get_sort_key)

    for idx, recipe in enumerate(recipes):
        print idx, "\\", recipe["name"], "\\", recipe["category"]


def get_sort_key(recipe):
    return recipe['category']

if __name__ == '__main__':
    print_recipes()
