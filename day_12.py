from copy import deepcopy

def tuple_equal(first,second):
    return first[0] == second[0] and first[1] == second[1] and first[2] == second[2]

def vector_of_tuples_equal(first,second):
    equal = True

    for i in range(len(first)):
        equal = equal and tuple_equal(first[i],second[i])
    return equal

def compute_energy(things, other_things):
    total = 0
    for i in range(len(things)):
        energy= (abs(things[i][0]) + abs(things[i][1]) + abs(things[i][2]))* (abs(other_things[i][0]) + abs(other_things[i][1]) + abs(other_things[i][2]))
        total= total + energy
    return total

def add_tuples(grav, distance_vector):
    return (grav[0] + distance_vector[0], grav[1] + distance_vector[1], grav[2] + distance_vector[2])

def clamp (value):
    return int(max(-1, min(1, value)))


if __name__ == '__main__':
    print("day twelve")

    positions = []
    '''
    positions.append((8, 0, 8))
    positions.append((0, -5, -10))
    positions.append((16, 10, -5))
    positions.append((19, -10, -7))
    
    positions.append((-1,  0,  2))
    positions.append(( 2,-10, -7))
    positions.append(( 4, -8,  8))
    positions.append(( 3,  5, -1))
    
    '''

    positions.append((-8, -10, 0))
    positions.append((5, 5,  10))
    positions.append((2, -7,  3))
    positions.append((9, -8, -3))


    initial_positions = deepcopy(positions)
    velocities = []
    for i in range(len(positions)):
        velocities.append((0,0,0))


    initial_velocities = deepcopy(velocities)


    for iteration in range(1000000000):
        for i in range(len(positions)):
            grav = (0,0,0)
            for j in range(len(positions)):
                if j == i:
                    continue
                distance_vector = (clamp(positions[j][0] - positions[i][0]),clamp(positions[j][1] - positions[i][1]),clamp(positions[j][2] - positions[i][2]))
                grav = add_tuples(grav,distance_vector)
            velocities[i] = add_tuples(grav,velocities[i])

        for i in range(len(positions)):
            positions[i] = add_tuples(positions[i], velocities[i])
        if (vector_of_tuples_equal(positions, initial_positions) and vector_of_tuples_equal(velocities,initial_velocities)):
            break
        if iteration % 1000000 == 0:
            print(iteration)

    print(iteration + 1)
    print(compute_energy(positions,velocities))
    #not 12036072









