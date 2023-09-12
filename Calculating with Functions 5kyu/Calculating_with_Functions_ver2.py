# Refactor

def zero(f=None):
    x = 0
    x = f(x) if f else x
    return x

def one(f=None):
    x = 1
    x = f(x) if f else x
    return x

def two(f=None):
    x = 2
    x = f(x) if f else x
    return x
    
def three(f=None):
    x = 3
    x = f(x) if f else x
    return x

def four(f=None):
    x = 4
    x = f(x) if f else x
    return x

def five(f=None):
    x = 5
    x = f(x) if f else x
    return x
    
def six(f=None):
    x = 6
    x = f(x) if f else x
    return x

def seven(f=None):
    x = 7
    x = f(x) if f else x
    return x

def eight(f=None):
    x = 8
    x = f(x) if f else x
    return x

def nine(f=None):
    x = 9
    x = f(x) if f else x
    return x

def plus(f):
    return lambda x: x+f

def minus(f):
    return lambda x: x-f

def times(f):
    return lambda x: x*f

def divided_by(f):
    return lambda x: x//f




if __name__=='__main__':
    print(two(times(five())))