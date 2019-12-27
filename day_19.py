def run_code_with_params(code_input, params, pc=0, rel_base=0):
    current_param = 0
    code = code_input  # .copy()
    # print(code)
    i = pc
    relative_base = rel_base
    output = []
    while i < len(code):
        if code[i] == 99:
            break
        op_as_string = str(code[i])
        if len(op_as_string) > 1:
            opcode = int(op_as_string[-2:])
        else:
            opcode = int(op_as_string[-1])

        first_param, second_param, third_param = None, None, None
        if len(op_as_string) > 2:
            first_param = process_param(code, op_as_string[-3], code[i + 1], relative_base)
            if len(op_as_string) > 3:
                second_param = process_param(code, op_as_string[-4], code[i + 2], relative_base)
                if len(op_as_string) > 4:
                    third_param = process_param(code, op_as_string[-5], code[i + 3], relative_base)

        if opcode == 1:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if len(op_as_string) < 5 or op_as_string[-5] == '0':
                code[code[i + 3]] = first_param + second_param
            else:
                code[code[i + 3] + relative_base] = first_param + second_param
            i = i + 4
            continue
        if opcode == 2:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if len(op_as_string) < 5 or op_as_string[-5] == '0':
                code[code[i + 3]] = first_param * second_param
            else:
                code[code[i + 3] + relative_base] = first_param * second_param
            i = i + 4
            continue
        if opcode == 3:
            if len(op_as_string) < 3 or op_as_string[-3] == '0':
                #code[code[i + 1]] = params[current_param]
                code[code[i + 1]] = params.pop(0)
            else:
                #code[code[i + 1] + relative_base] = params[current_param]
                code[code[i + 1] + relative_base] = params.pop(0)
            current_param = current_param + 1
            i = i + 2
            continue
        if opcode == 4:
            if first_param is None:
                first_param = code[code[i + 1]]
            # print(first_param)
            # output.append(first_param)
            i = i + 2
            return (first_param, i, relative_base)
            continue
        if opcode == 5:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if first_param != 0:
                i = second_param
                continue
            else:
                i = i + 3
                continue
        if opcode == 6:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if first_param == 0:
                i = second_param
                continue
            else:
                i = i + 3
                continue
        if opcode == 7:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if first_param < second_param:
                op_result = 1
            else:
                op_result = 0
            if len(op_as_string) < 5 or op_as_string[-5] == '0':
                code[code[i + 3]] = op_result
            else:
                code[code[i + 3] + relative_base] = op_result
            i = i + 4
        if opcode == 8:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if first_param == second_param:
                op_result = 1
            else:
                op_result = 0
            if len(op_as_string) < 5 or op_as_string[-5] == '0':
                code[code[i + 3]] = op_result
            else:
                code[code[i + 3] + relative_base] = op_result
            i = i + 4
        if opcode == 9:
            if first_param is None:
                first_param = code[code[i + 1]]
            relative_base = relative_base + first_param
            i = i + 2
        if opcode == 99:
            print('HALT OP')
            return (-1, -1, -1)
            break

    return -1, -1, -1


def process_param(code, param_char, param_value, relative_base):
    if param_char == '0':
        first_param = code[param_value]
    elif param_char == '1':
        first_param = param_value
    elif param_char == '2':
        first_param = code[param_value + relative_base]
    return first_param


def get_value_at_coord(code, x,y):
    value, _, _ = run_code_with_params(code.copy(), [x,y], 0, 0)
    return value

def ones_to_the_right_of(x,y,code):
    current_x = x + 1
    current_value = get_value_at_coord(code,current_x,y)
    count = 0
    while current_value != 0:
        count = count + 1
        current_x = current_x + 1
        current_value = get_value_at_coord(code,current_x,y)
    return count

def ones_below_of(x,y,code):
    current_y = y + 1
    current_value = get_value_at_coord(code,x,current_y)
    count = 0
    while current_value != 0:
        count = count + 1
        current_y = current_y + 1
        current_value = get_value_at_coord(code,x,current_y)

    return count


if __name__ == '__main__':
    print("day nineteen")

    code = []
    with open('day_19.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    for i in range(100):
        code.append(0)

    original_code = code.copy()

    out_pc = 0
    out_rel_base = 0

    image = [[]]

    current_line_index = 0
    IMAGE_SIZE = 100

    params = []


    current_x = 900
    current_y = 450

    TARGET_SQUARE_SIZE = 100
    while True:
        #print((current_x, current_y))

        ones_right = ones_to_the_right_of(current_x,current_y,code)
        ones_below = ones_below_of(current_x,current_y,code)

        if ones_right >= 99 and ones_below >= 99:
            print((current_x, current_y))
            exit(0)
        else:
            if ones_right > ones_below:
                current_x = current_x + 1
            else:
                current_y = current_y + 1


    #not 10200560