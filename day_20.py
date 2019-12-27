from curses.ascii import isalnum


def add_connections_in_line(LINE,FOLLOWING_LINE,ACTUAL_ANCHOR_LINE, image, connections,outer=False):
    for i in range(len(image[LINE])):
        if isalnum(image[LINE][i]):
            name = image[LINE][i] + image[FOLLOWING_LINE][i]
            coord = (ACTUAL_ANCHOR_LINE, i)
            if image[coord[0]][coord[1]]!= '.':
                raise Exception()
            if name not in connections.keys():
                if outer:
                    connections[name] = (coord, None)
                else:
                    connections[name] = (None, coord)
            else:
                if outer:
                    connections[name] = (coord, connections[name][1])
                else:
                    connections[name] = (connections[name][0], coord)

def add_connections_in_column(LINE,FOLLOWING_LINE,ACTUAL_ANCHOR_LINE, image, connections,outer=False):
    for i in range(len(image)):
        if len(image[i]) <= LINE:
            continue
        if isalnum(image[i][LINE]):
            name = image[i][LINE] + image[i][FOLLOWING_LINE]
            coord = (i, ACTUAL_ANCHOR_LINE)
            if image[coord[0]][coord[1]]!= '.':
                raise Exception()
            if name not in connections.keys():
                if outer:
                    connections[name] = (coord, None)
                else:
                    connections[name] = (None, coord)
            else:
                if outer:
                    connections[name] = (coord, connections[name][1])
                else:
                    connections[name] = (connections[name][0], coord)


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

if __name__ == '__main__':
    print("day twenty")

    image = []
    with open('day_20.txt', 'r') as input_file:
        line = input_file.readline()[:-1]
        while len(line) > 2:
            image.append(list(line))
            line = input_file.readline()[:-1]

    for line in image:
        print(line)


    connections = dict()
    add_connections_in_line(0,1,2,image,connections, True)
    add_connections_in_line(27, 28, 26, image, connections)
    add_connections_in_line(80, 81, 82, image, connections)
    add_connections_in_line(107,108, 106, image, connections,True)
    add_connections_in_column(0, 1, 2, image, connections,True)
    add_connections_in_column(27, 28, 26, image, connections)
    add_connections_in_column(78, 79, 80, image, connections)
    add_connections_in_column(105, 106, 104, image, connections,True)

    print(connections)

    pending_paths = []

    min_steps_to_reach = dict()

    current_position = (connections['AA'][0][0],connections['AA'][0][1],0)

    destination = (connections['ZZ'][0][0],connections['ZZ'][0][1],0)

    connection_locations = dict()
    level_changes = dict()
    for connection_name in connections.keys():
        first, second = connections[connection_name]
        if first is not None and second is not None:
            level_changes[first] = -1
            level_changes[second] = 1
            connection_locations[first] = second
            connection_locations[second] = first



    #current_step_count = 0

    min_steps_to_reach[current_position] = 0
    while current_position != destination:

        up = (current_position[0], current_position[1] - 1,current_position[2])
        down = (current_position[0], current_position[1] + 1,current_position[2])
        left = (current_position[0] - 1, current_position[1],current_position[2])
        right = (current_position[0] + 1, current_position[1],current_position[2])


        possible_moves = [up,down,left,right]
        curr_pos_no_level = (current_position[0],current_position[1])
        if curr_pos_no_level in connection_locations.keys():
            if level_changes[curr_pos_no_level] != -1 or current_position[2] > 0:
                other_side_position = connection_locations[curr_pos_no_level]
                possible_moves.append((other_side_position[0],other_side_position[1],current_position[2] + level_changes[curr_pos_no_level]))

        i = 0
        while i < len(possible_moves):
            candidate_location = possible_moves[i]

            if image[candidate_location[0]][candidate_location[1]] != '.':
                possible_moves.pop(i)
            elif candidate_location in min_steps_to_reach.keys():
                min_steps_to_reach[candidate_location] = min(min_steps_to_reach[candidate_location], min_steps_to_reach[current_position] + 1)
                possible_moves.pop(i)
            else:
                min_steps_to_reach[candidate_location] = min_steps_to_reach[current_position] + 1
                i = i + 1

        if len(possible_moves) == 0:
            current_position = pending_paths.pop(0)
        else:
            current_position = possible_moves.pop(0)
            pending_paths.extend(possible_moves)

        print(current_position)


    print(min_steps_to_reach[destination])





