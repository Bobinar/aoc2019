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
                code[code[i + 1]] = ord(params.pop(0))
            else:
                #code[code[i + 1] + relative_base] = params[current_param]
                code[code[i + 1] + relative_base] = ord(params.pop(0))
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

def next_thing_in_direction(direction_vector, current_position, image):
    next_position = (direction_vector[0] + current_position[0], direction_vector[1] + current_position[1])
    if next_position[0] < 0 or next_position[0] >= len(image[0]) or next_position[1] < 0 or next_position[1] >= len(image):
        return '.'
    else:
        return image[next_position[1]][next_position[0]]


def direction_to_vector(direction):
    direction_vector = None
    if direction == 0:
        direction_vector = (0, -1)
    elif direction == 1:
        direction_vector = (1, 0)
    elif direction == 2:
        direction_vector = (0, 1)
    elif direction == 3:
        direction_vector = (-1, 0)
    return direction_vector


def direction_change_as_string(current_direction, new_direction):
    if new_direction %4 == (current_direction + 1 ) %4:
        return 'R'
    if new_direction % 4 == (current_direction - 1) % 4:
        return 'L'
    raise Exception("erroraco")


if __name__ == '__main__':
    print("day seventeen")

    code = []
    with open('day_17.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    for i in range(100000):
        code.append(0)

    original_code = code.copy()

    out_pc = 0
    out_rel_base = 0

    image = [[]]

    current_line_index = 0

    while out_pc != -1:
        x, out_pc, out_rel_base = run_code_with_params(code, [], out_pc, out_rel_base)
        if out_pc == -1:
            break
        if x != 10:
            image[current_line_index].append(chr(x))
        else:
            image.append([])
            current_line_index = current_line_index + 1
    image.pop()
    image.pop()



    intersections = []
    sum_alignment = 0
    for j in range(1,len(image)-1):
        for i in range(1,len(image[j])-1):
            if image[j][i] == '#' and image[j-1][i] == '#' and image[j+1][i] == '#' and image[j][i-1] == '#' and image[j][i+1] == '#':
                intersections.append((i,j))
                alignment = i*j
                sum_alignment = sum_alignment + alignment
                #image[j][i] = 'O'

    for line in image:
        print(line)

    print(sum_alignment)

    #second part

    start_pos = None
    for j in range(len(image)):
        for i in range(len(image[j])):
            if image[j][i] == '^':
                start_pos = (i,j)
                break

    current_pos = start_pos
    current_direction = 0 # 0 up, 1 right, ...

    current_input = "R"
    current_direction = 1
    while True:
        positions_moved = 0
        direction_vector = direction_to_vector(current_direction)
        while next_thing_in_direction(direction_vector,current_pos,image) != '.':
            positions_moved = positions_moved + 1
            current_pos = (current_pos[0] + direction_vector[0], current_pos[1] + direction_vector[1])
            image[current_pos[1]][current_pos[0]] = 'V'
        current_input = current_input + ',' + str(positions_moved)
        other_directions = [0,1,2,3]
        other_directions.remove(current_direction)
        c = 0
        while c < len(other_directions):
            if next_thing_in_direction(direction_to_vector(other_directions[c]),current_pos,image) != '#':
                other_directions.remove(other_directions[c])
            else:
                c = c + 1


        for line in image:
            print(line)

        if len(other_directions) == 0:
            print('finished')
            break
        current_input = current_input + ',' + direction_change_as_string(current_direction,other_directions[0])
        current_direction = other_directions[0]


    print(current_input)



    #'R,6,L,8,R,8,R,6,L,8,R,8,R,4,R,6,R,6,R,4,R,4,L,8,R,6,L,10,L,10,R,4,R,6,R,6,R,4,R,4,L,8,R,6,L,10,L,10,R,4,R,6,R,6,R,4,R,4,L,8,R,6,L,10,L,10,R,6,L,8,R,8,L,8,R,6,L,10,L,10'

    A = 'R,4,R,6,R,6,R,4,R,4'

    B = 'L,8,R,6,L,10,L,10'


    C = 'R,6,L,8,R,8'




    current_input = current_input.replace(A,'A')
    current_input = current_input.replace(B,'B')
    current_input = current_input.replace(C,'C')

    print(current_input)

    out_pc = 0
    out_rel_base = 0
    code = original_code
    code[0] = 2

    total_input = list(current_input + '\n' + A + '\n' + B + '\n' + C + '\n' + 'n\n')


    while out_pc != -1:
        x, out_pc, out_rel_base = run_code_with_params(code, total_input, out_pc, out_rel_base)
        if out_pc == -1:
            break
        print(x)







