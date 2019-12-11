from math import gcd
from math import atan2
from math import pi


def calculate_visible_asteroids(candidate_asteroid, asteroids):


    direction_to_asteroids = dict()
    for asteroid in asteroids:
        if asteroid == candidate_asteroid:
            continue
        direction = (asteroid[0] - candidate_asteroid[0],asteroid[1] - candidate_asteroid[1])
        divider = gcd(abs(direction[0]),abs(direction[1]))
        simplified_direction = (int(direction[0]/divider), int(direction[1]/divider))
        if simplified_direction in direction_to_asteroids.keys():
            direction_to_asteroids[simplified_direction].append(asteroid)
        else:
            direction_to_asteroids[simplified_direction] = [asteroid]


    return (len(direction_to_asteroids.keys()),direction_to_asteroids)




if __name__ == '__main__':
    print("day nine")

    asteroid_map = []
    asteroids = []
    with open('day_10.txt', 'r') as input_file:

        line = input_file.readline()

        while len(line) > 0:
            map_line = []

            for char in line:
                if char == '#':
                    asteroids.append((len(map_line),len(asteroid_map)))
                    map_line.append('#')

                elif char == '.':
                    map_line.append('.')
            #print(map_line)
            asteroid_map.append(map_line)
            line = input_file.readline()

    #print(asteroids)
    current_max = 0
    best_asteroid = None
    best_directions_to_asteroid = None
    for asteroid in asteroids:
        visible_asteroids, directions_to_asteroid = calculate_visible_asteroids(asteroid, asteroids)
        if visible_asteroids > current_max:
            current_max = visible_asteroids
            best_asteroid = asteroid
            best_directions_to_asteroid = directions_to_asteroid

    print(current_max)
    print(best_asteroid)

    directions = list(best_directions_to_asteroid.keys())
    directions_sorted = sorted(directions, key=lambda x: (pi - atan2(x[0],x[1])))

    current_direction_index = 0
    destroyed_asteroids = 0
    while destroyed_asteroids < 200:
        direction_to_shoot = None
        while(direction_to_shoot is None):
            if directions_sorted[current_direction_index] in best_directions_to_asteroid.keys():
                direction_to_shoot = directions_sorted[current_direction_index]
                current_direction_index = (current_direction_index + 1) % len(directions_sorted)
                break
            else:
                current_direction_index = (current_direction_index + 1) % len(directions_sorted)
        #get closest asteroid in that direction

        closest_asteroid_in_direction = None
        candidate_asteroids = best_directions_to_asteroid[direction_to_shoot]
        closest_distance = 1000000
        for candidate_asteroid in candidate_asteroids:
            distance_vector = (candidate_asteroid[0] - best_asteroid[0],candidate_asteroid[1] - best_asteroid[1] )
            distance_squared = distance_vector[0] * distance_vector[0] + distance_vector[1] * distance_vector[1]
            if distance_squared < closest_distance:
                closest_asteroid_in_direction = candidate_asteroid
                closest_distance = distance_squared

        #destroy asteroid
        best_directions_to_asteroid[direction_to_shoot].remove(closest_asteroid_in_direction)
        if len(best_directions_to_asteroid[direction_to_shoot]) == 0:
            directions_sorted.remove(direction_to_shoot)
            # will fail if current_direction_index = 0
            current_direction_index = current_direction_index - 1

        destroyed_asteroids = destroyed_asteroids + 1

    print(closest_asteroid_in_direction)









