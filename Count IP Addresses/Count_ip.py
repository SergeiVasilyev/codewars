# First solution. Convert all numbers to hex, combine and then get a difference between numbers
def ips_between(start, end):
    st_ip = list(map(lambda x: hex(int(x)).split('x')[-1].zfill(2), start.split(".")))
    st_ip_hex_num = ''.join(st_ip)
    
    end_ip = list(map(lambda x: hex(int(x)).split('x')[-1].zfill(2), end.split(".")))
    end_ip_hex_num = ''.join(end_ip)

    return int(end_ip_hex_num, 16) - int(st_ip_hex_num, 16)

# Second solution. Сalculate the decimal number by multiplying each byte by 256 to the power of the position of this byte
# First byte 256**0, Second 256**1...
def ips_between2(start, end):
    start, end = start.split('.'), end.split('.')
    sum_start, sum_end = 0, 0

    # Make loop from 0 to 4
    for n in range(0, 4):
        sum_start += int(start[n]) * (256**abs(n-3)) # Reverse the power from 3 to 0
        sum_end += int(end[n]) * (256**abs(n-3)) # Reverse the power from 3 to 0
    
    sum_ip_adresses = sum_end - sum_start

    return sum_ip_adresses



if __name__=='__main__':
    print('First solution')
    print("10.0.0.0 -", "10.0.0.50 =", ips_between("10.0.0.0", "10.0.0.50"))
    print("20.0.0.0 -", "20.0.2.0 =", ips_between("20.0.0.0", "20.0.2.0"))
    print("10.0.0.255 -", "10.0.1.0 =", ips_between("10.0.0.255", "10.0.1.0"))

    print('\nSecond solution')
    print("10.0.0.0 -", "10.0.0.50 =", ips_between2("10.0.0.0", "10.0.0.50"))
    print("20.0.0.0 -", "20.0.2.0 =", ips_between2("20.0.0.0", "20.0.2.0"))
    print("10.0.0.255 -", "10.0.1.0 =", ips_between2("10.0.0.255", "10.0.1.0"))

