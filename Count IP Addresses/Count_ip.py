def ips_between(start, end):
    st_ip = list(map(lambda x: hex(int(x)).split('x')[-1].zfill(2), start.split(".")))
    st_ip_hex_num = ''.join(st_ip)
    
    end_ip = list(map(lambda x: hex(int(x)).split('x')[-1].zfill(2), end.split(".")))
    end_ip_hex_num = ''.join(end_ip)

    return int(end_ip_hex_num, 16) - int(st_ip_hex_num, 16)



if __name__=='__main__':
    print(ips_between("10.0.0.0", "10.0.0.50"))
    print(ips_between("20.0.0.0", "20.0.2.0"))
    print(ips_between("10.0.0.255", "10.0.1.0"))

