from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30, price_range=(5, 10), weight_range=(5, 100)):
    """Generate n number of products within a specified price and weight range"""
    products = []
    for i in range(1, n + 1):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randrange(price_range[0], price_range[1] + 1)
        weight = random.randrange(weight_range[0], weight_range[1] + 1)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append(product)
    return products


def inventory_report(prod_list):
    """Creates an inventory report for a given product list"""
    prod_list = list(set(prod_list))
    x = 0
    price = 0
    weight = 0
    flammability = 0
    stealability = 0
    for item in prod_list:
        x += 1
        price += item.price
        weight += item.weight
        flammability += item.flammability
        if stealability != 'Not so stealable...':
            stealability += 1

    avg_price = price / x
    avg_weight = weight / x
    avg_flammability = flammability / x
    print(f'There are {x} unique products in this list. The average price is {avg_price}, '
          f'average weight is {avg_weight},'
          f'and the average flammability is {avg_flammability}.')
    if stealability >= len(prod_list) / 2:
        print('Many of these items are highly stealable!')
    return avg_price, avg_weight, avg_flammability


if __name__ == '__main__':
    inventory_report(generate_products())
