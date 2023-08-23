import os

file = open("folder1/filename1x.txt", "w")
file.write("Primera línea" + os.linesep)
file.write("Segunda línea")
file.close()

#chmod 444 folder1