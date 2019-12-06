
def two_adjacent_digits_are_the_same(number):
    string = str(number)
    for i in range(len(string) - 1):
        #print(i)
        if string[i] == string[i+1] \
                and (((i+2) >= len(string)) or (string[i+2] != string[i])) \
                and (((i-1) < 0) or (string[i-1] != string[i])):
            return True
    return False

def never_decreases(number):
    string = str(number)

    for i in range(len(string) - 1):
        if string[i] > string[i+1]:
            return False
    return True



if __name__ == '__main__':
    print("day four")

    min_number = 246540
    max_number = 787419

    possible_numbers = 0
    for i in range(min_number, max_number):
        if two_adjacent_digits_are_the_same(i) and never_decreases(i):
            possible_numbers = possible_numbers + 1

    print(possible_numbers)

