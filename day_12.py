from copy import deepcopy
from math import gcd


def lcm(a, b,c):
    """Compute the lowest common multiple of a and b"""
    print(a*b*c)
    print(gcd(a, gcd(b, c)))
    return a * b * c / int(gcd(a, gcd(b, c)))

def list_equal(first,second):
    return first[0] == second[0] and first[1] == second[1] and first[2] == second[2]

def vector_of_lists_equal(first,second):
    equal = True

    for i in range(len(first)):
        equal = equal and list_equal(first[i],second[i])
    return equal

def compute_energy(things, other_things):
    total = 0
    for i in range(len(things)):
        energy= (abs(things[i][0]) + abs(things[i][1]) + abs(things[i][2]))* (abs(other_things[i][0]) + abs(other_things[i][1]) + abs(other_things[i][2]))
        total= total + energy
    return total

def add_lists(grav, distance_vector, result):
    result[0] = grav[0] + distance_vector[0]
    result[1] = grav[1] + distance_vector[1]
    result[2] = grav[2] + distance_vector[2]

def clamp (value):
    return int(max(-1, min(1, value)))


def sim_coord(positions_in, velocities_in):
    finish = False
    iteration = 0
    velocities = deepcopy(velocities_in)
    positions = deepcopy(positions_in)
    positions_next = deepcopy(positions)
    initial_positions = deepcopy(positions)
    initial_velocities = deepcopy(velocities)
    solutions = 0
    while not finish:
        for i in range(len(positions)):
            for j in range(len(positions)):
                if j == i:
                    continue
                velocities[i] = velocities[i] + clamp(positions[j] - positions[i])
            positions_next[i] = positions[i] + velocities[i]
        aux = positions
        positions = positions_next
        positions_next = aux
        if iteration % 100000000000000 == 0:
            print(iteration)
            print(str(positions) + '\t' + str(velocities))
        if positions == initial_positions and velocities == initial_velocities:
            print('--------------')
            print(iteration + 1)
            print('--------------')
            solutions = solutions + 1
            #if solutions >= 100:
            #    return
            return
        iteration = iteration + 1



if __name__ == '__main__':
    print("day twelve")

    print(lcm(18,28,44))

    positions = []

    positions.append([8, 0, 8   ])
    positions.append([0, -5, -10])
    positions.append([16, 10, -5])
    positions.append([19, -10,-7])

    '''
    positions.append([-1,  0,  2])
    positions.append([ 2,-10, -7])
    positions.append([ 4, -8,  8])
    positions.append([ 3,  5, -1])

    
    
    positions.append([-8, -10,0])
    positions.append([5, 5,  10])
    positions.append([2, -7,  3])
    positions.append([9, -8, -3])
    392733896255168
    '''
    velocities = []
    for i in range(len(positions)):
        velocities.append([0, 0, 0])

    for j in range(3):
        print('solutions for ' + str(j))
        sim_coord([x[j] for x in positions],[x[j] for x in velocities])

    exit()

    initial_positions = deepcopy(positions)

    positions_next = deepcopy(positions)
    initial_velocities = deepcopy(velocities)

    print(str(positions[:][0]) + '\t' + str(velocities[:][0]))
    reported = [False,False,False]
    finish = False
    iteration = 0
    while not finish:
        for i in range(len(positions)):
            for j in range(len(positions)):
                if j == i:
                    continue
                velocities[i][0] = velocities[i][0] + clamp(positions[j][0] - positions[i][0])
                velocities[i][1] = velocities[i][1] + clamp(positions[j][1] - positions[i][1])
                velocities[i][2] = velocities[i][2] + clamp(positions[j][2] - positions[i][2])
            add_lists(positions[i], velocities[i],positions_next[i])
        aux = positions_next
        positions_next = positions
        positions = aux
        #if iteration % 1 == 0:
            #print(iteration)
        #    print(str(positions[:][0]) + '\t' + str(velocities[:][0]))

        for j in range(3):
            if reported[j]:
                continue
            if (list_equal(positions[:][j], initial_positions[:][j]) and list_equal(velocities[:][j], initial_velocities[:][j])):
                reported[j] = True
                print('--------------')
                print('coordinate ' + str(j))
                print(iteration + 1)
                print('--------------')

                #print(positions)
                #print(velocities)
        if reported[0] and reported[1] and reported[2]:
            finish = True
        iteration = iteration + 1


    print('------------------')



    print(iteration)
    print(compute_energy(positions,velocities))
    #not 12036072









