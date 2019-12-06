
def look_for_SAN_in_subtree(nodeNameToChildren, current_node):
    if current_node == 'SAN':
        return 0
    else:
        if current_node not in nodeNameToChildren.keys():
            return -1
        children = nodeNameToChildren[current_node]
        for child in children:
            distance = look_for_SAN_in_subtree(nodeNameToChildren, child)
            if distance != -1:
                return distance + 1
        return -1


if __name__ == '__main__':
    print("day six")
    nodeNameToParent = dict()
    nodeNameToChildren = dict()
    with open('day_6_2_p.txt', 'r') as input_file:
        line = input_file.readline()
        while len(line) > 0:
            line = line.replace('\n','')
            parts = line.split(')')
            if parts[0] in nodeNameToChildren.keys():
                nodeNameToChildren[parts[0]].append(parts[1])
            else:
                nodeNameToChildren[parts[0]] = [parts[1]]
            nodeNameToParent[parts[1]] = parts[0]
            line = input_file.readline()
    '''
    total_orbits = 0
    for nodeName in nodeNameToParent.keys():
        current_node = nodeName
        while current_node is not None:
            if current_node not in nodeNameToParent.keys():
                current_node = None
            else:
                current_node = nodeNameToParent[current_node]
                total_orbits = total_orbits + 1
    print(total_orbits)
    '''

    distance_upwards = 0
    distance_downwards = -1
    current_node = nodeNameToParent['YOU']
    while distance_downwards == -1:
        distance_downwards = look_for_SAN_in_subtree(nodeNameToChildren, current_node)
        if distance_downwards != -1:
            print(distance_downwards + distance_upwards)
            break
        else:
            distance_upwards = distance_upwards + 1
            current_node = nodeNameToParent[current_node]

    # substract 1 from printed number