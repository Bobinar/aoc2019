

def run_code_with_params(code_input, p1, p2):
    code = code_input.copy()
    #print(code)
    code[1] = p1
    code[2] = p2

    for i in range(0,len(code),4):
        if code[i] == 99:
            break
        if code[i] == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
            continue
        if code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
            continue

    return code[0]



if __name__ == '__main__':
    print("day two")

    #code = [1,9,10,3,2,3,11,0,99,30,40,50]
    code = []
    with open('day_2.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        for op in ops:
            code.append(int(op))

    for p1 in range(100):
        for p2 in range(100):
            result = run_code_with_params(code,p1,p2)
            if result == 19690720:
                print(p1)
                print(p2)


