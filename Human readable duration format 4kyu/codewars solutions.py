# 1
def format_duration(seconds):

    if seconds is 0: return 'now'
	
    scale = [
        ('second',          1),
        ('minute',         60),
        ('hour',        60*60),
        ('day',      60*60*24),
        ('year', 60*60*24*365) ]
       
    times = []
    for n, s in reversed(scale):
        t = seconds/s
        if t: times.append((t,n+'s' if t > 1 else n))
        seconds = seconds%s
        
    if len(times) > 1:
        return ', '.join('%d %s' % t for t in times[:-1]) + ' and %d %s' % times[-1]
    else:
        return '%d %s' % times[0]
    


# 2
def f(n, unit):
    return [', ', '{} {}{}'.format(n, unit, 's' if n > 1 else '')]

def format_duration(seconds):
    if not seconds: return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    fs = []
    if years: fs.extend(f(years, 'year'))
    if days: fs.extend(f(days, 'day'))
    if hours: fs.extend(f(hours, 'hour'))
    if minutes: fs.extend(f(minutes, 'minute'))
    if seconds: fs.extend(f(seconds, 'second'))

    fs[-2] = ' and '
    fs.pop(0)
    return ''.join(fs)