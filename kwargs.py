# kwargs = parameter will pack all arguments into a dictionery
#              useful so that a function can accept a varying amount of keywords arguments

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Md.", middle="Selim", last="Reja")
