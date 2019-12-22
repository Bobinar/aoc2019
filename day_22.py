

def deal_new(old_stack):
    new_stack = []

    i = len(old_stack) - 1

    while i >= 0:
        new_stack.append(old_stack[i])
        i = i - 1

    return new_stack

def cut(number, old_stack):
    new_stack = []
    if number > 0:
        for i in range(number, len(old_stack)):
            new_stack.append(old_stack[i])

        for i in range(number):
            new_stack.append(old_stack[i])
    else:
        for i in range(len(old_stack) + number, len(old_stack)):
            new_stack.append(old_stack[i])

        for i in range(len(old_stack) + number):
            new_stack.append(old_stack[i])
    return new_stack


def deal_increment(number, old_stack):
    new_stack = [-1] * len(old_stack)
    read_index, write_index = 0, 0

    while read_index < len(old_stack):
        new_stack[write_index] = old_stack[read_index]

        read_index = read_index + 1

        write_index = (write_index + number) % len(old_stack)


    return new_stack




if __name__ == '__main__':
    print("day fourteen")

    DEAL_NEW_TEXT = 'deal into new stack'
    CUT_TEXT = 'cut '
    DEAL_INCREMENT_TEXT = 'deal with increment '

    DEAL_NEW = 0
    CUT = 1
    DEAL_INCREMENT = 2


    rules_dict = dict()
    code = []

    operations = []
    with open('day_22.txt', 'r') as input_file:
        line = input_file.readline()[:-1]
        while len(line) > 2:

            if CUT_TEXT in line:
                number = int(line.replace(CUT_TEXT,''))
                operations.append((CUT,number))
            elif DEAL_INCREMENT_TEXT in line:
                number = int(line.replace(DEAL_INCREMENT_TEXT, ''))
                operations.append((DEAL_INCREMENT, number))
            elif DEAL_NEW_TEXT in line:
                operations.append((DEAL_NEW, 0))
            line = input_file.readline()[:-1]

    print(operations)


    DECK_SIZE = 10007

    current_stack = list(range(DECK_SIZE))
    print(current_stack)
    for op in operations:
        print(op)
        if op[0] == DEAL_NEW:
            current_stack = deal_new(current_stack)
        elif op[0] == CUT:
            current_stack = cut(op[1],current_stack)
        elif op[0] == DEAL_INCREMENT:
            current_stack = deal_increment(op[1], current_stack)


        print(current_stack)

    print(current_stack)

    print(current_stack.index(2019))
