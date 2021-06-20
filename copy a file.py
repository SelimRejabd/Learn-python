# copyfile() = copies contents of a file
# copy() = copyfile( ) + permission mode + destination can be a direction
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('F:\\CSE\\Python programs\\text.txt', 'F:\\CSE\\copy.txt')
