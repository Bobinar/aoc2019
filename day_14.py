import math

leftovers_dict = dict()

def ore_needed_to_make_product(product, quantity_needed, rules_dict):
    #if product in speed_dict.keys():
    #    return speed_dict[product]
    if product == 'ORE':
        #print('USED {} ORE'.format(quantity_needed))
        return quantity_needed
    quantity_produced_per_reaction, ingredientotes = rules_dict[product]
    production = 0
    ore_cost = 0
    quantity_to_produce = quantity_needed - leftovers_dict[product]
    #print('STARTING to make {} of {}'.format(quantity_needed,product))
    while production < quantity_to_produce:
        if leftovers_dict[product] > 0:
            #print('USING NEW LEFTOVERS of {}'.format(product))
            production = production + leftovers_dict[product]
            leftovers_dict[product] = 0
            continue

        for ingredient in ingredientotes:
            leftover_quantity = leftovers_dict[ingredient[0]]
            if ingredient[1] < leftover_quantity:
                leftovers_dict[ingredient[0]] = leftovers_dict[ingredient[0]] - ingredient[1]
                #print('USING {} leftovers of {}'.format(ingredient[1],ingredient[0]))
            else:
                leftovers_dict[ingredient[0]] = 0
                #if leftover_quantity > 0:
                    #print('USING {} leftovers of {} but still need to make more'.format(leftover_quantity, ingredient[0]))
                ore_cost = ore_cost + ore_needed_to_make_product(ingredient[0],ingredient[1] - leftover_quantity,rules_dict)
        #print('MADE batch of {} {}'.format(quantity_produced_per_reaction, product))
        production = production + quantity_produced_per_reaction

    #print('making '+ str(quantity_produced_per_reaction) + ' ' + str(product) + ' costs ' + str(ore_cost_per_reaction) + ' ore')

    leftover = production - quantity_needed
    #if leftover > 0:
    #   print('ADDING {} leftover {}'.format(leftover,product))
    leftovers_dict[product] = leftovers_dict[product] + leftover
    return ore_cost





if __name__ == '__main__':
    print("day fourteen")

    rules_dict = dict()
    code = []
    with open('day_14.txt', 'r') as input_file:
        line = input_file.readline()[:-1]
        while len(line) > 2:
            split_line = line.split(' => ')
            ingredients_string = split_line[0]
            product_string = split_line[1]

            product_split = product_string.split(' ')
            product_quantity = int(product_split[0])
            product_name = product_split[1]
            leftovers_dict[product_name] = 0

            ingredients = []
            for ingredient_string in ingredients_string.split(', '):
                print(ingredient_string)
                ingredient_split = ingredient_string.split(' ')
                ingredient_quantity = int(ingredient_split[0])
                ingredient_name = ingredient_split[1]
                ingredients.append((ingredient_name,ingredient_quantity))
            if product_name in rules_dict.keys():
                raise Exception("product already in dict")
            rules_dict[product_name] = (product_quantity, ingredients)

            line = input_file.readline()[:-1]

    leftovers_dict['ORE'] = 0
    fuel_ingredients = rules_dict['FUEL']

    ore_quantity = 0

    ore_remaining = 1000000000000
    fuel_produced = 0


    fuel_per_seed_round = 10000
    ore_needed_to_make_first_fuel_round = ore_needed_to_make_product('FUEL', fuel_per_seed_round, rules_dict)
    #ore_remaining = ore_remaining - ore_needed_to_make_first_fuel

    leftovers_from_first_fuel = leftovers_dict.copy()
    leftovers_99 = dict()

    rounds_needed = int(ore_remaining / ore_needed_to_make_first_fuel_round)

    rounds_99 = int(rounds_needed * 0.999)


    for product in leftovers_from_first_fuel.keys():
        leftovers_99[product] = leftovers_from_first_fuel[product] * rounds_99

    ore_remaining = ore_remaining - (rounds_99 * ore_needed_to_make_first_fuel_round)

    leftovers_dict = leftovers_99
    fuel_produced = rounds_99 * fuel_per_seed_round


    while ore_remaining > 0:
        ore_needed = ore_needed_to_make_product('FUEL',1, rules_dict)
        if ore_needed < ore_remaining:
            fuel_produced = fuel_produced + 1
            ore_remaining  = ore_remaining - ore_needed
            print(ore_remaining)
        else:
            break
    print(fuel_produced)
    print(leftovers_dict)


    # not 62201705059
    # not 64429
    #2035 too low

    #part 2 5192851 too low