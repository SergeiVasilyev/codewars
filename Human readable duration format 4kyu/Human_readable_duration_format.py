def format_duration(s):
    h = s // 60**2
    seconds = s % 60
    mins = s // 60 % 60
    hours = h % 24
    days = h // 24 % 365
    years = h // 24 // 365
    date_name = ['year', 'day', 'hour', 'minute', 'second']

    def plural_indicator(num) -> str:
        if num > 1: return 's'
        return ''
    
    def time_format(*dur_list):
        f = ''
        for key, l in enumerate(dur_list):
            et_or_comma = (", " if sum(dur_list[key+1:])!=0 else " and ") if f != "" else ""
            if l: f += f'{et_or_comma}{l} {date_name[key]}{plural_indicator(l)}'

        return f if f else 'now'

    return time_format(years, days, hours, mins, seconds)



if __name__=='__main__':
    print(format_duration(3601)) # 1:00:01
    print(format_duration(3925)) # 1:06:25
    print(format_duration(86399)) # 23:59:59
    print(format_duration(86400)) # 1 day 
    print(format_duration(31535999)) # 364 days, 23:59:59
    print(format_duration(31536000)) # 1 year
    print(format_duration(31536060)) # 1 year 1 min


