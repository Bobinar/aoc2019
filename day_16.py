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

        numbers_list = [int(v) for v in line_as_list]



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
    for i in range(100):

        next_input = []
        for phase_index in range(len(numbers_list)):

            total = 0
            for digit_index in range(len(numbers_list)):
                pattern_value = calculate_pattern_value(digit_index, phase_index)
                total = total + numbers_list[digit_index] * pattern_value
            sum_value = int(str(total)[-1])
            next_input.append(sum_value)
        #print(next_input)
        numbers_list = next_input
    print(numbers_list)