import keyboard
import os

def run_code_with_params(code_input, params,pc=0, rel_base=0):
    current_param = 0
    code = code_input#.copy()
    #print(code)
    i = pc
    relative_base = rel_base
    output = []
    while i < len(code):
        if code[i] == 99:
            break
        op_as_string = str(code[i])
        if len(op_as_string) >1:
            opcode = int(op_as_string[-2:])
        else:
            opcode = int(op_as_string[-1])

        first_param, second_param, third_param = None, None, None
        if len(op_as_string) > 2:
            first_param = process_param(code, op_as_string[-3], code[i+1], relative_base)
            if len(op_as_string) > 3:
                second_param = process_param(code, op_as_string[-4], code[i+2], relative_base)
                if len(op_as_string) > 4:
                    third_param = process_param(code, op_as_string[-5], code[i+3], relative_base)

        if opcode == 1:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i+2]]
            if len(op_as_string) < 5 or op_as_string[-5] == '0':
                code[code[i+3]] = first_param + second_param
            else:
                code[code[i + 3] + relative_base] = first_param + second_param
            i = i + 4
            continue
        if opcode == 2:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i+2]]
            if len(op_as_string) < 5 or op_as_string[-5] == '0':
                code[code[i+3]] = first_param * second_param
            else:
                code[code[i + 3] + relative_base] = first_param * second_param
            i = i + 4
            continue
        if opcode == 3:
            if len(op_as_string) <3 or op_as_string[-3] == '0':
                code[code[i+1]] = params[current_param]
            else:
                code[code[i + 1] + relative_base] = params[current_param]
            current_param = current_param + 1
            i = i + 2
            continue
        if opcode == 4:
            if first_param is None:
                first_param = code[code[i + 1]]
            #print(first_param)
            #output.append(first_param)
            i = i + 2
            return (first_param,i,relative_base)
            continue
        if opcode == 5:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i+2]]
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
                code[code[i + 3]+relative_base] = op_result
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

    return  -1, -1,-1


def process_param(code, param_char, param_value, relative_base):
    if param_char == '0':
        first_param = code[param_value]
    elif param_char == '1':
        first_param = param_value
    elif param_char == '2':
        first_param = code[param_value + relative_base]
    return first_param


def try_combination(combination, input_code):
    codes = []
    pcs = []
    for i in range(5):
        codes.append(input_code.copy())
        pcs.append(0)

    previous_output = 0
    current_outputs = [0]*5

    while pcs[4] != -1:
        for i in range(len(combination)):
            phase_value = combination[i]
            previous_output, pc = run_code_with_params(codes[i], [phase_value,previous_output] if pcs[i] == 0 else [previous_output], pcs[i])
            pcs[i] = pc
            if pc != -1:
                current_outputs[i] = previous_output

    return current_outputs[4]

if __name__ == '__main__':
    print("day thirteen")

    code = []
    with open('day_13.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    for i in range(100000):
        code.append(0)


    current_position = (0,0)

    current_direction = 0 # 0=up, 1=right, 2=down, 3=left

    current_tile_color = 1 # 0=black, 1=white

    out_pc=0
    out_rel_base=0

    paint_dict = dict()
    min_x = 10000
    min_y = 10000
    max_x = 0
    max_y = 0
    current_score = 0
    current_input = 0
    block_count = -1
    ball_position = (0,0)
    paddle_position = (0,0)
    ball_going_right = False

    while out_pc != -1:
        x, out_pc, out_rel_base = run_code_with_params(code, [current_input], out_pc, out_rel_base)
        if out_pc == -1:
            break
        y, out_pc, out_rel_base = run_code_with_params(code, [current_input], out_pc, out_rel_base)
        tile_id, out_pc, out_rel_base = run_code_with_params(code, [current_input], out_pc, out_rel_base)
        if x == -1 and y == 0:
            current_score = tile_id
            print(current_score)
            continue

        paint_dict[(x,y)] = tile_id
        if x > max_x:
            max_x  = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
        if tile_id == 4:
            ball_position = (x,y)

        if tile_id == 3:
            paddle_position = (x,y)

        if tile_id == 4 or tile_id == 3:
            if ball_position[0] > paddle_position[0]:
                current_input = 1
            elif ball_position[0] < paddle_position[0]:
                current_input = -1
            else:
                current_input = 0
            print('-------------------')
            print('ball ' + str(ball_position))
            print('paddle ' + str(paddle_position))
            print(current_input)

    block_count = 0
    image = []
    for i in range(24):
        image.append([])
        for j in range(42):
            value = 0 if (j, i) not in paint_dict.keys() else paint_dict[(j, i)]
            if value == 4:
                if ball_position[0] < j:
                    ball_going_right = True
                else:
                    ball_going_right = False
                ball_position = (j, i)
            if value == 3:
                paddle_position = (j, i)

            #char = ' ' if value == 0 else '#'
            if value == 2:
                block_count = block_count + 1
            char = str(value)
            image[i].append(char)

        #print(image[i])
    print('--------')
    print(ball_position)
    print(paddle_position)




