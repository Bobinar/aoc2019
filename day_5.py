

def run_code_with_params(code_input, p1):
    code = code_input.copy()
    #print(code)
    i = 0
    while i < len(code):
        if code[i] == 99:
            break
        op_as_string = str(code[i])
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
            code[code[i+1]] = p1
            i = i + 2
            continue
        if opcode == 4:
            if first_param is None:
                first_param = code[code[i + 1]]
            print(first_param)
            i = i + 2
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


if __name__ == '__main__':
    print("day five")

    #code = [1,9,10,3,2,3,11,0,99,30,40,50]
    code = []
    with open('day_5_2.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    run_code_with_params(code,5)

