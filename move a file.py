import os

source = "F:\\CSE\\copy.txt"
destination = "F:\\CSE\\Python programs\\copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")

except FileExistsError as e:
    print(e)
