# 1 Using eval()

# def zero(arg=""):  return eval("0" + arg)
# def one(arg=""):   return eval("1" + arg)
# def two(arg=""):   return eval("2" + arg)
# def three(arg=""): return eval("3" + arg)
# def four(arg=""):  return eval("4" + arg)
# def five(arg=""):  return eval("5" + arg)
# def six(arg=""):   return eval("6" + arg)
# def seven(arg=""): return eval("7" + arg)
# def eight(arg=""): return eval("8" + arg)
# def nine(arg=""):  return eval("9" + arg)

# def plus(n):       return '+' + str(n)
# def minus(n):      return '-' + str(n)
# def times(n):      return '*' + str(n)
# def divided_by(n): return '//' + str(n)


# 2 Solution with lambda functions
# id_ = lambda x: x
# number = lambda x: lambda f=id_: f(x)
# zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
# print(two())
# plus = lambda x: lambda y: y + x
# minus = lambda x: lambda y: y - x
# times = lambda x: lambda y: y * x
# divided_by = lambda x: lambda y: y // x



# 3 Lambda functions modified to normal functons
def id_(x):
    return x

def number(x):
    def fun(f=id_):
        return f(x)
    return fun

zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))

def plus(x):
    def sub_plus(y):
        return y+x
    return sub_plus

def minus(x):
    def sub_minus(y):
        return y+x
    return sub_minus

def times(x):
    def sub_times(y):
        return y*x
    return sub_times

def divided_by(x):
    def sub_divided_by(y):
        return y//x
    return sub_divided_by



if __name__=='__main__':
    print(two(times(five())))
    print(four(times(five())))
    print(four(plus(five())))
    print(eight(divided_by(four())))