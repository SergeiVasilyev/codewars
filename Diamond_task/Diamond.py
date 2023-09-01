def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    
    diamond_str = ''
    for i in range(1, n+1, 2):
        space_mult = round((n-i) / 2)
        diamond_str += (' ' * space_mult) + ('*' * i) + '\n'

    for i in range(n-2, 0, -2):
        space_mult = round((n-i) / 2)
        diamond_str += (' ' * space_mult) + ('*' * i) + '\n'

    return diamond_str

if __name__ == '__main__':
    print(diamond(7))