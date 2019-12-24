import math

def calculate_biodiverisity(input):
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):

            if input[i][j] == '#':
                index = i * 5 + j
                total = total + int(pow(2,index))
    return total

def create_empty_level():
    input = []
    input.append(['.', '.', '.', '.', '.'])
    input.append(['.', '.', '.', '.', '.'])
    input.append(['.', '.', '?', '.', '.'])
    input.append(['.', '.', '.', '.', '.'])
    input.append(['.', '.', '.', '.', '.'])
    return input

if __name__ == '__main__':
    print("day twenty four")

    input = []
    input.append(['#','#','.','#','.'])
    input.append(['#','#','.','#','.'])
    input.append(['#','#','?','#','#'])
    input.append(['.','#','#','#','#'])
    input.append(['.','#','.','.','.'])

    #input.append(['.','.','.','.','#'])
    #input.append(['#','.','.','#','.'])
    #input.append(['#','.','?','#','#'])
    #input.append(['.','.','#','.','.'])
    #input.append(['#','.','.','.','.'])

    biodiversities = set()

    next_input = [cosa.copy() for cosa in input]
    next_input = [create_empty_level(),next_input, create_empty_level()]
    input = [create_empty_level(),input, create_empty_level()]

    #current_biodiversity = calculate_biodiverisity(input)
    steps = 0
    while steps < 200:#current_biodiversity not in biodiversities:
        #biodiversities.add(current_biodiversity)
        for level in range(len(input)):
            for i in range(len(input[level])):
                for j in range(len(input[level][i])):
                    if i == 2 and j == 2:
                        continue

                    #part 1 rules
                    bugs_adjacent = 0
                    if i > 0 and input[level][i - 1][j] == '#':
                        bugs_adjacent = bugs_adjacent + 1
                    if i < (len(input[level]) - 1) and input[level][i + 1][j] == '#':
                        bugs_adjacent = bugs_adjacent + 1
                    if j > 0 and input[level][i][j - 1] == '#':
                        bugs_adjacent = bugs_adjacent + 1
                    if j < (len(input[level][i]) - 1) and input[level][i][j + 1] == '#':
                        bugs_adjacent = bugs_adjacent + 1

                    #borders with higher level
                    if level > 0:
                        if i == 0 and input[level-1][1][2] == '#':
                            bugs_adjacent = bugs_adjacent + 1
                        if i == len(input[level]) -1 and input[level-1][3][2] == '#':
                            bugs_adjacent = bugs_adjacent + 1
                        if j == 0 and input[level-1][2][1] == '#':
                            bugs_adjacent = bugs_adjacent + 1
                        if j == len(input[level][i]) - 1 and input[level - 1][2][3] == '#':
                            bugs_adjacent = bugs_adjacent + 1

                    #borders with lower level
                    if level < (len(input) -1):
                        lower_level = level + 1
                        if i == 1 and j == 2:
                            for cell in input[lower_level][0]:
                                if cell == '#':
                                    bugs_adjacent = bugs_adjacent + 1
                        if i == 3 and j == 2:
                            for cell in input[lower_level][4]:
                                if cell == '#':
                                    bugs_adjacent = bugs_adjacent + 1

                        if i == 2 and j == 1:
                            for row_index in range(len(input[lower_level])):
                                if input[lower_level][row_index][0] == '#':
                                    bugs_adjacent = bugs_adjacent + 1
                        if i == 2 and j == 3:
                            for row_index in range(len(input[lower_level])):
                                if input[lower_level][row_index][4] == '#':
                                    bugs_adjacent = bugs_adjacent + 1

                    if input[level][i][j] == '#':
                        if bugs_adjacent != 1:
                            next_input[level][i][j] = '.'
                        else:
                            next_input[level][i][j] = '#'

                    if input[level][i][j] == '.':
                        if bugs_adjacent ==1 or bugs_adjacent == 2:
                            next_input[level][i][j] = '#'
                        else:
                            next_input[level][i][j] = '.'

        #current_biodiversity = calculate_biodiverisity(next_input)

        aux = input
        input = next_input
        next_input = aux
        steps = steps + 1

        input.insert(0,create_empty_level())
        next_input.insert(0,create_empty_level())
        input.append(create_empty_level())
        next_input.append(create_empty_level())

    total_bugs = 0
    mid = math.floor(len(input)/2)
    for level_index in range(len(input)):
        level = input[level_index]
        print('level ' + str(level_index - mid))
        for i in range(len(level)):
            print(level[i])
            for j in range(len(level[i])):

                if level[i][j] == '#':
                    total_bugs = total_bugs + 1

    print(total_bugs)

    #print(current_biodiversity)




