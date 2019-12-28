def calculate_pattern_value(digit_index, phase_index):
    pattern = [0, 1, 0, -1]


    return pattern[int((digit_index + 1)/(phase_index + 1)) % 4]



if __name__ == '__main__':
    print("day sixteen")

    rules_dict = dict()
    code = []
    with open('day_16.txt', 'r') as input_file:
        line = input_file.readline()
        line_as_list = list(line)

        numbo_list = [int(v) for v in line_as_list]



    #numbers_list = list('80871224585914546619083218645595')
    #numbers_list = [int(v) for v in numbers_list]

    # test pattern
    '''
    for phase_index in range(len(numbers_list)):
        line = 'phase {} : '.format(phase_index)
        for digit_index in range(len(numbers_list)):
            line = line + str(calculate_pattern_value(digit_index, phase_index)) + ', '
        print(line)
    '''
    '''
    numbers_list = numbo_list
    for phase_index in range(len(numbers_list)):
        different_offsets = []
        period = 4 * (phase_index + 1)
        for burr in range(10000):
            start_index = 650 *burr
            offset = start_index % period
            if offset not in different_offsets:
                different_offsets.append(offset)
        print(len(different_offsets))
    '''

    pattern = [0, 1, 0, -1]

    numbers_list = []
    for i in range(10000):
        numbers_list.extend(numbo_list)
    next_input = numbers_list.copy()
    string_offset = ''
    for i in range(7):
        string_offset = string_offset + str(numbo_list[i])
    message_offset = int(string_offset)
    if message_offset <= len(numbers_list)/2:
        raise Exception("fast way wont work")
    current_input = numbers_list
    for _ in range(100):

        next_input[-1] = current_input[-1]
        i = len(current_input) - 2
        while i >= message_offset:
            next_input[i] = (next_input[i+1] + current_input[i]) % 10
            i = i -1
        #print(next_input)
        aux = current_input
        current_input = next_input
        next_input = aux
    print(numbers_list[message_offset:message_offset + 8])

    #not 30817365
