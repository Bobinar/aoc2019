

def run_code_with_params(code_input, params,pc):
    current_param = 0
    code = code_input#.copy()
    #print(code)
    i = pc
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
            first_param = code[code[i+1]] if op_as_string[-3] == '0' else code[i+1]
            if len(op_as_string) > 3:
                second_param = code[code[i+2]] if op_as_string[-4] == '0' else code[i+2]
                if len(op_as_string) > 4:
                    third_param = code[code[i + 3]] if op_as_string[-5] == '0' else code[i + 3]

        if opcode == 1:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i+2]]
            code[code[i+3]] = first_param + second_param
            i = i + 4
            continue
        if opcode == 2:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i+2]]

            code[code[i+3]] = first_param * second_param
            i = i + 4
            continue
        if opcode == 3:
            code[code[i+1]] = params[current_param]
            current_param = current_param + 1
            i = i + 2
            continue
        if opcode == 4:
            if first_param is None:
                first_param = code[code[i + 1]]
            #print(first_param)
            #output.append(first_param)
            i = i + 2
            return (first_param,i)
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
                code[code[i+3]] = 1
            else:
                code[code[i+3]] = 0
            i = i + 4
        if opcode == 8:
            if first_param is None:
                first_param = code[code[i + 1]]
            if second_param is None:
                second_param = code[code[i + 2]]
            if first_param == second_param:
                code[code[i + 3]] = 1
            else:
                code[code[i + 3]] = 0
            i = i + 4
        if opcode == 99:
            return (-1, -1)
            break

    return  -1, -1
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
    print("day seven")

    code = []
    with open('day_7.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    combinations = []
    power = 0
    for i in range(5,10):
        for j in range (5,10):
            if j == i:
                continue
            for k in range (5,10):
                if k == j or k == i:
                    continue
                for l in range(5,10):
                    if l == k or l == j or l == i:
                        continue
                    for m in range(5,10):
                        if m == l or m == k or m == j or m == i:
                            continue
                        power = max(power, try_combination([i,j,k,l,m], code))
    print(power)





