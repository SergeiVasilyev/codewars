import operator

def zero(f=None):
    x = 0
    x = f[0](x, f[1]) if f else x
    return x

def one(f=None):
    x = 1
    x = f[0](x, f[1]) if f else x
    return x

def two(f=None):
    x = 2
    x = f[0](x, f[1]) if f else x
    return x
    
def three(f=None):
    x = 3
    x = f[0](x, f[1]) if f else x
    return x

def four(f=None):
    x = 4
    x = f[0](x, f[1]) if f else x
    return x

def five(f=None):
    x = 5
    x = f[0](x, f[1]) if f else x
    return x
    
def six(f=None):
    x = 6
    x = f[0](x, f[1]) if f else x
    return x

def seven(f=None):
    x = 7
    x = f[0](x, f[1]) if f else x
    return x

def eight(f=None):
    x = 8
    x = f[0](x, f[1]) if f else x
    return x

def nine(f=None):
    x = 9
    x = f[0](x, f[1]) if f else x
    return x

def plus(f):
    return operator.add, f

def minus(f):
    return operator.sub, f

def times(f):
    return operator.mul, f

def divided_by(f):
    return operator.floordiv, f




if __name__=='__main__':
    print(two(times(five())))