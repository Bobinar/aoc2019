from curses.ascii import isalnum
memo = dict()

def has_key(key, keys_string):
    key_index = ord(key) - 97
    return keys_string[key_index] == 1

def set_key(key,value,keys_string):
    key_index = ord(key) - 97
    new_string = ''# + keys_string
    for i in range(len(keys_string)):
        if i != key_index:
            new_string = new_string + keys_string[i]
        else:
            new_string = new_string + ('1' if value == 1 else '0')
    #new_string[key_index] = value
    return new_string

def active_keys(key_string):
    result = []
    for i in range(len(key_string)):
        if key_string[i] == '1':
            result.append(chr(i + 97))
    return result

def find_best_path_recursive(current_keys,keys_left,keys_to_all):
    if (current_keys,keys_left) in memo.keys():
        return memo[(current_keys,keys_left)]

    candidate_keys = active_keys(keys_left)
    if len(candidate_keys) == 0:

        return (0,'')


    min_steps = None

    for bot_index in range(4):
        current_key = current_keys[bot_index]
        keys_to_consider = keys_to_all[current_key]

        for candidate_key in candidate_keys:  # keys_to_consider.keys():
            if candidate_key == current_key or candidate_key not in keys_to_consider:
                continue
            distance, keys_needed = keys_to_consider[candidate_key]
            can_go_there = True
            for key_needed in keys_needed:
                if key_needed.lower() in candidate_keys:
                    can_go_there = False
                    break
            if can_go_there:
                #new_keys_left = keys_left.copy()
                #new_keys_left.remove(candidate_key)
                new_keys_left = set_key(candidate_key,0,keys_left)

                new_candidate_keys = (current_keys[0] if bot_index != 0 else candidate_key,current_keys[1]  if bot_index != 1 else candidate_key,current_keys[2]  if bot_index != 2 else candidate_key,current_keys[3]  if bot_index != 3 else candidate_key)

                rest_of_steps, combination = find_best_path_recursive(new_candidate_keys,new_keys_left,keys_to_all)
                if rest_of_steps is None:
                    continue
                new_steps = distance + rest_of_steps
                if min_steps == None or new_steps < min_steps:
                    min_steps = new_steps
                    best_combination = candidate_key + combination
                min_steps = min(min_steps, new_steps)

    memo[(current_keys,keys_left)] = (min_steps, best_combination)
    return (min_steps, best_combination)

def search_all_reachable_keys(image,from_position):
    current_position = from_position
    min_steps_to_reach = dict()
    min_steps_to_reach[current_position] = 0
    pending_paths = []
    current_keys_needed = []

    reachable_keys_to_moves = dict()
    while True:
        current_cell = image[current_position[0]][current_position[1]]
        if ord(current_cell) >= ord('A') and ord(current_cell) <= ord('Z') and current_cell not in current_keys_needed:
            current_keys_needed.append(current_cell)

        up = (current_position[0], current_position[1] - 1)
        down = (current_position[0], current_position[1] + 1)
        left = (current_position[0] - 1, current_position[1])
        right = (current_position[0] + 1, current_position[1])

        possible_moves = [up, down, left, right]

        i = 0
        while i < len(possible_moves):
            candidate_location = possible_moves[i]

            candidate_cell = image[candidate_location[0]][candidate_location[1]]
            if candidate_cell == '#':
                possible_moves.pop(i)
            elif candidate_location!= from_position and ord(candidate_cell) >= ord('a') and ord(candidate_cell) <= ord('z'):
                if candidate_cell in reachable_keys_to_moves.keys():
                    reachable_keys_to_moves[candidate_cell] = (min(reachable_keys_to_moves[candidate_cell][0],
                                                                  min_steps_to_reach[current_position] + 1), current_keys_needed.copy())
                else:
                    reachable_keys_to_moves[candidate_cell] = (min_steps_to_reach[current_position] + 1,current_keys_needed.copy())
                #possible_moves.pop(i)
                min_steps_to_reach[candidate_location] = min_steps_to_reach[current_position] + 1
                i = i + 1
            elif candidate_location in min_steps_to_reach.keys():
                min_steps_to_reach[candidate_location] = min(min_steps_to_reach[candidate_location],
                                                             min_steps_to_reach[current_position] + 1)
                possible_moves.pop(i)
            else:
                min_steps_to_reach[candidate_location] = min_steps_to_reach[current_position] + 1
                i = i + 1

        if len(possible_moves) == 0:
            if len(pending_paths) == 0:
                break
            current_position, current_keys_needed = pending_paths.pop(0)
        else:
            current_position = possible_moves.pop(0)
            pending_paths.extend([(m,current_keys_needed.copy()) for m in possible_moves])
    return reachable_keys_to_moves

if __name__ == '__main__':
    print("day eighteen")

    image = []
    with open('day_18_2.txt', 'r') as input_file:
        line = input_file.readline()[:-1]
        while len(line) > 2:
            image.append(list(line))
            line = input_file.readline()[:-1]


    for line in image:
        print(line)

    key_locations = dict()
    door_locations = dict()

    starting_points = []

    for i in range(len(image)):
        for j in range(len(image[i])):
            current_position = (i,j)
            if image[i][j] == '@':
                image[i][j] = '.'
                starting_points.append(current_position)
            if isalnum(image[i][j]):
                if ord(image[i][j]) < 97:
                    #it's upper case
                    door_locations[image[i][j]] = current_position
                else:
                    key_locations[image[i][j]] = current_position


    print(starting_points)


    keys_all = list(key_locations.keys())

    keys_to_all = dict()

    keys_to_all['@1'] = search_all_reachable_keys(image, starting_points[0])
    keys_to_all['@2'] = search_all_reachable_keys(image, starting_points[1])
    keys_to_all['@3'] = search_all_reachable_keys(image, starting_points[2])
    keys_to_all['@4'] = search_all_reachable_keys(image, starting_points[3])

    for key in keys_all:
        keys_to_all[key] = search_all_reachable_keys(image,key_locations[key])


    min_steps = 100000000000
    current_key = '@'
    key_cosa = ''
    for i in range(len(keys_all)):
        key_cosa = key_cosa + '1'
    print(find_best_path_recursive(('@1','@2','@3','@4'), key_cosa,keys_to_all))



