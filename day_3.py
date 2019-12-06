
def build_set_from_ops(ops):
    first_set = set()
    current_position = (0, 0)
    distance = 0
    position_to_distance = dict()
    for op in ops:
        if op[0] == 'R':
            direction = (1, 0)
        if op[0] == 'L':
            direction = (-1, 0)
        if op[0] == 'U':
            direction = (0, 1)
        if op[0] == 'D':
            direction = (0, -1)

        magnitude = int(op[1:])
        for i in range(magnitude):
            current_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            first_set.add(current_position)
            distance = distance + 1
            if not current_position in position_to_distance.keys():
                position_to_distance[current_position] = distance
    return first_set, position_to_distance


if __name__ == '__main__':
    print("day three")

    #code = [1,9,10,3,2,3,11,0,99,30,40,50]
    code = []
    with open('day_3.txt', 'r') as input_file:
        line = input_file.readline()
        ops = line.split(',')
        first_set, first_position_to_distance= build_set_from_ops(ops)
        line = input_file.readline()
        ops = line.split(',')
        second_set, second_position_to_distance= build_set_from_ops(ops)

    intersections = first_set.intersection(second_set)
    print(intersections)
    min = 1000000
    min_position = None

    for intersection in intersections:
        #distance = abs(intersection[0]) + abs(intersection[1])
        distance = first_position_to_distance[intersection] + second_position_to_distance[intersection]
        if distance < min:
            min = distance
            min_position = intersection
    print(min)
    print(min_position)





