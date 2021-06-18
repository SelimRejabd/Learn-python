# args = parameter that will pack all arguments into a tuple
#       usefull so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum


print(add(1, 2, 3, 4))
