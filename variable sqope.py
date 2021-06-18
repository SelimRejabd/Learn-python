# sqope = The region that a variabel is recognized
#       A  variable is only available from inside the region it is created.
#       A gloabal and locally scoped versions of a variable can be created

name = "Reja"  # This is global sqope ( available inside and outside functions)


def display_name():
    name = "Selim"  # local variable (only available in function)
    print(name)


display_name()
print(name)
