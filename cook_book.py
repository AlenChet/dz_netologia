from pprint import pprint


def read_cook_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        cook_book = {}
        for i in f:
            name = i.strip()
            quantity = int(f.readline().strip())
            ingredients = []
            for ingredient in range(quantity):
                ing_line = {}
                ing = f.readline().split(' | ')
                ing_line['ingredient_name'] = ing[0].strip()
                ing_line['quantity'] = ing[1].strip()
                ing_line['measure'] = ing[2].strip()
                ingredients.append(ing_line)
            f.readline()
            cook_book[name] = ingredients
    return cook_book


cook_book = read_cook_book('reciptes.txt')
# pprint(cook_book)


