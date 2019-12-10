def recursive_fuel(mass):
    if mass <= 0:
        return 0
    fuel = int(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + recursive_fuel(fuel)


if __name__ == '__main__':
    total = 0
    with open("first_input.txt", 'r') as input_file:
        new_line = input_file.readline()
        while(len(new_line) > 0):
            mass = int(new_line)

            total = total + recursive_fuel(mass)
            new_line = input_file.readline()


    print(total)
