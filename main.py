from pprint import pprint

def cook_book_dict(file_cook_book):
    cook_book = {}
    with open(file_cook_book, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            counter = file.readline()
            cook_book[dish_name] = []
            for i in range(int(counter)):
                ingredient, quantity, unit = file.readline().split(' | ')
                cook_book[dish_name].append({
                    'ingredient_name': ingredient,
                    'quantity': int(quantity),
                    'measure': unit.strip()
                })
            file.readline()
    return cook_book
pprint(cook_book_dict('cook_book.txt'))

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = cook_book_dict('cook_book.txt')
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
            else:
                shop_list[ingredient_name]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list
pprint(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос', 'Запеченный картофель'], 2))