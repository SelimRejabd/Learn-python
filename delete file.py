import os
import shutil

path = "D:\\pip"

try:
    os.rmdir(path)
    shutil.rmtree(path)  # if the file is not empty
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("you can't delete this folder using this function")
else:
    print(path + " was deleted")
