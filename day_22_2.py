import math

DECK_SIZE = 119315717514047

def deal_new_reverse(target_position):

    return (DECK_SIZE -1) - target_position

def cut_reverse(number, target_position):
    new_stack = []
    if number > 0:

        if target_position >= (DECK_SIZE - number):
            return target_position - (DECK_SIZE - number)
        else:
            return target_position + number
    else:
        cut_size = -(number)

        if target_position >= cut_size:
            return  (target_position - cut_size)
        else:
            return (target_position + (DECK_SIZE - cut_size))

    return None


def deal_increment_reverse(step_size, target_position):
    read_index = 0
    min_steps_in_loop = math.floor(DECK_SIZE/step_size)
    offset_needed = target_position % step_size
    current_offset = 0

    while current_offset != offset_needed:
        #how much are we going to jump?
        read_index = read_index + min_steps_in_loop
        candidate_step = current_offset + min_steps_in_loop * step_size
        if candidate_step < DECK_SIZE:
            read_index = read_index + 1
            candidate_step = candidate_step + step_size
        current_offset = candidate_step % DECK_SIZE

    read_index = read_index + ((target_position - current_offset) / step_size)

    return int(read_index)




if __name__ == '__main__':
    print("day fourteen")
    deal_increment_reverse(3,1)

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




    #current_stack = list(range(DECK_SIZE))
    #print(current_stack)
    operations.reverse()
    target_position = 2020
    for iteration in range(101741582076661):
        for op in operations:
            #print(op)
            if op[0] == DEAL_NEW:
                target_position = deal_new_reverse(target_position)
            elif op[0] == CUT:
                target_position = cut_reverse(op[1],target_position)
            elif op[0] == DEAL_INCREMENT:
                target_position = deal_increment_reverse(op[1], target_position)
            #print(current_stack)
        #print(target_position)
        if iteration % 10000 == 0:
            print(iteration)
            print(target_position)

    #print(current_stack)
    print(target_position)
    #print(current_stack.index(2020))
