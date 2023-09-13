# odd = True if not reduce(lambda a, b: a * b, integers[:3]) % 2 else False
# odd = True if not reduce(lambda a, b: (a % 2) ^ (b % 2), integers[:3]) else False


start = "10.0.0.0"

st_ip = list(map(int, start.split(".")))
st_ip_hex = list(map(lambda x: hex(x).split('x')[-1], st_ip))
st_ip_hex2 = list(map(lambda x: hex(x), st_ip))
print(st_ip_hex2[0] + st_ip_hex2[1], 0xa)
