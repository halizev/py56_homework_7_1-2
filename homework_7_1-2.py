# homework_7_1
from pprint import pprint
cook_book = dict()


def file_to_dict(file):
    with open(file, encoding='utf8') as file_obj:
        file_list = file_obj.read().split('\n')
        line_count = 0
        line_count_max = int(len(file_list))
        while line_count < line_count_max:
            cook_book[file_list[line_count]] = []
            ingredient_count = 0
            ingredient_count_max = int(file_list[line_count + 1])
            while ingredient_count < ingredient_count_max:
                ingredient_list = file_list[line_count + ingredient_count + 2].split(' | ')
                ingredient_dict = dict()
                ingredient_dict['ingredient_name'] = ingredient_list[0]
                ingredient_dict['quantity'] = ingredient_list[1]
                ingredient_dict['measure'] = ingredient_list[2]
                cook_book[file_list[line_count]].append(ingredient_dict)
                ingredient_count += 1
            line_count += ingredient_count_max + 3
    return cook_book


pprint(file_to_dict('recipes.txt'))
print('_________________________________________________________________________________________')
print('homework_7_2')
print('_________________________________________________________________________________________')

# homework_7_2
shop_list = dict()


def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for recipe in cook_book[dish]:
            ingredient_name = recipe['ingredient_name']
            if ingredient_name not in shop_list.keys():
                recipe_quantity = int(recipe['quantity']) * person_count
                shop_list[ingredient_name] = {'measure': recipe['measure'], 'quantity': recipe_quantity}
            else:
                shop_list[ingredient_name]['quantity'] += int(recipe['quantity']) * person_count
    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
