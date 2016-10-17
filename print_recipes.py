from parse import parse


def print_recipes(recipes):
    for idx, recipe in enumerate(recipes):
        # prints the recipes, doesn't return stuff
        print idx, "\\", recipe["name"], "\\", recipe["category"]


if __name__ == '__main__':
    recipes = parse()

    print_recipes(recipes)
