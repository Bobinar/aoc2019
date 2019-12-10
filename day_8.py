



if __name__ == '__main__':
    print("day eight")
    width = 25
    height = 6

    layers = []


    with open('day_8.txt', 'r') as input_file:
        line = input_file.readline()
        current_char = 0
        layer_size = width * height
        num_layers = int(len(line)/layer_size)

        for layer_number in range(num_layers):
            layer = []
            for pixel_number in range(layer_size):
                layer.append(int(line[current_char]))
                current_char = current_char + 1
            layers.append(layer)
    '''
    min_zeros_layer = -1
    min_zeros = 1000000

    for layer in layers:
        zeros_in_layer = layer.count(0)
        if zeros_in_layer < min_zeros:
            min_zeros_layer = layer
            min_zeros = zeros_in_layer

    print(min_zeros_layer.count(1) * min_zeros_layer.count(2))
    '''
    final_image = [-1] * width * height

    for i in range(len(final_image)):

        for layer in layers:
            if layer[i] != 2:
                final_image[i] = layer[i]
                if final_image[i] == 0:
                    final_image[i] = ' '
                else:
                    final_image[i] = '1'

                break

    for i in range(height):
        print(final_image[i*width : (i+1)* width])
    #EJRGP


