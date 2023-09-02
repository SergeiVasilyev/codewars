def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    
    diamond_str = ''
    for i in range(n):
        space_multiplier = abs((n // 2) - i)
        star_multiplier = n - abs((n - 1) - i * 2)
        diamond_str += (' ' * space_multiplier) + ('*' * star_multiplier) + '\n'

    return diamond_str

if __name__ == '__main__':
    print(diamond(9))