from parse import parse
from print_recipes import print_recipes


def listr():
    recipe_list = parse()
    print_recipes(recipe_list)

    # get inputs from user and stores them as int
    menu = raw_input(
        'Which recipes do you want to make? Enter their indices, separated by commas:')
    index_input = menu.split(',')
    index_list = [int(x.strip()) for x in index_input]
    print index_list

    print '\r\n', 'Here is your grocery list', '\r\n'

    # select those indexes from the recipe list
    subset_menu = list(recipe_list[i] for i in index_list)

    merged_ingredients = {}

    for recipe in subset_menu:
        for ingredient in recipe['ingredients']:

            name = ingredient['name']
            # check if it is in merged_ingredients
            if name not in merged_ingredients:
                merged_ingredients[name] = ingredient
            else:
                m_ingredient = merged_ingredients[name]
                # if yes, check the "unit", if units match, add them
                if ingredient['unit'] == m_ingredient['unit']:
                    merged_ingredients[name]['amount'] += ingredient['amount']

    # prints a complete sum ingredient item as (amount, unit, name)
    for ingredient in sorted(merged_ingredients.values(), key=get_sort_key):
        print ingredient['amount'], ingredient['unit'], ingredient['name']


def get_sort_key(ingredient):
    return ingredient['name']

if __name__ == '__main__':
    listr()
