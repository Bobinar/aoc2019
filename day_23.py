
def run_code_with_params(code_input, params,pc=0, rel_base=0, stepmode= False):
    #current_param = 0
    code = code_input#.copy()

    i = pc
    relative_base = rel_base
    output = []

    start_pc = pc
    while i < len(code) and (not stepmode or i == start_pc):
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
            if len(params) == 0:
                return (None,i,relative_base)
            else:
                param_value = params.pop(0)
            if len(op_as_string) <3 or op_as_string[-3] == '0':
                code[code[i+1]] = param_value
            else:
                code[code[i + 1] + relative_base] = param_value
            #current_param = current_param + 1
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
            continue
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
            continue
        if opcode == 9:
            if first_param is None:
                first_param = code[code[i + 1]]
            relative_base = relative_base + first_param
            i = i + 2
            continue
        if opcode == 99:
            print('HALT OP')
            return (-1, -1, -1)
            break
        raise Exception("unknown opcode " + str(opcode))
    if i < len(code):
        return (None,i,relative_base)
    else:
        return  -1, -1,-1


def process_param(code, param_char, param_value, relative_base):
    if param_char == '0':
        first_param = code[param_value]
    elif param_char == '1':
        first_param = param_value
    elif param_char == '2':
        first_param = code[param_value + relative_base]
    return first_param


if __name__ == '__main__':
    print("day twenty three")

    code = []
    with open('day_23.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    for i in range(100000):
        code.append(0)

    NUM_COMPUTERS = 50
    out_pcs=[0] * NUM_COMPUTERS
    out_rel_bases= [0] *NUM_COMPUTERS
    input_queues = []
    codes = []
    for i in range(NUM_COMPUTERS):
        input_queues.append([i])
        codes.append(code.copy())

    nat_x, nat_y = -1, -1
    last_y_value_sent = None

    while not all(out_pc == -1 for out_pc in out_pcs):
        if all(len(queue) == 0 for queue in input_queues):
            input_queues[0].append(nat_x)
            input_queues[0].append(nat_y)
            if last_y_value_sent == nat_y:
                print(last_y_value_sent)
                exit(0)
            last_y_value_sent = nat_y

        for c in range(NUM_COMPUTERS):
            if out_pcs[c] != -1:
                pc_before = out_pcs[c]
                send_address, out_pcs[c], out_rel_bases[c] = run_code_with_params(codes[c], input_queues[c], out_pcs[c], out_rel_bases[c],False)
                if pc_before == out_pcs[c]:
                    input_queues[c].append(-1)
                    send_address, out_pcs[c], out_rel_bases[c] = run_code_with_params(codes[c], input_queues[c],
                                                                                      out_pcs[c], out_rel_bases[c],
                                                                                      False)
                if send_address != None:
                    if out_pcs[c] == -1:
                        continue
                    x, out_pcs[c], out_rel_bases[c] = run_code_with_params(codes[c], input_queues[c], out_pcs[c],
                                                                                      out_rel_bases[c],False)
                    y, out_pcs[c], out_rel_bases[c] = run_code_with_params(codes[c], input_queues[c], out_pcs[c],
                                                                           out_rel_bases[c], False)
                    if send_address == 255:
                        nat_x = x
                        nat_y = y
                    else:
                        input_queues[send_address].append(x)
                        input_queues[send_address].append(y)






