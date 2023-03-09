from pprint import pprint
from cook_book import cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for key, value in cook_book.items():
            if dish == key:
                for ingredient in value:
                    name = ingredient['ingredient_name']
                    measure = ingredient['measure']
                    quantity = int(ingredient['quantity']) * person_count
                    if name not in shop_list:
                        shop_list[name] = {'measure': measure,
                                           'quantity': quantity}
                    else:
                        shop_list[name]['quantity'] += quantity
    return shop_list


shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
# pprint(shop_list)

