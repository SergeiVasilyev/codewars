def hex_string_to_RGB(hex_string):
    if len(hex_string) != 7 and hex_string[0] != '#':
        raise ValueError("Value must be in the format #FFAABB")
    hex_string = hex_string[1:7]
    R = int(hex_string[:2], 16)
    G = int(hex_string[2:4], 16)
    B = int(hex_string[4:], 16)
    rgb = {'r': R, 'g': G, 'b': B}
    return rgb




if __name__ == '__main__':
    print(hex_string_to_RGB('#FF25Ag'))
