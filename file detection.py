import os

path = "F:\\CSE\\Python programs\\text.txt"
#path = "F:\\CSE\\Python programs"

if os.path.exists(path):
    print("That's location exists")
    if os.path.isfile(path):
        print("That's a file")
    elif os.path.isdir(path):
        print("That's a directory")

else:
    print("That's location doesn't exists")
