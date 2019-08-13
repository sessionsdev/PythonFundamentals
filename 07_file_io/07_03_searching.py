'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''
import os

list_of_jpg = []
list_of_files = []
target = ".jpg"

folder = "/home/jonathan/Documents/photos"


for i in os.listdir(folder):
    if i.endswith(target):
        list_of_jpg.append(i)
    list_of_files.append(i)

print(list_of_jpg)
print(list_of_files)