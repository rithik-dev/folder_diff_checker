# Python 3.9.6

import tkinter as tk
from tkinter import filedialog
import os

files_dir1 = set()
files_dir2 = set()


def check_difference():
    dir1_extra_files = list(files_dir1 - files_dir2)
    dir2_extra_files = list(files_dir2 - files_dir1)

    # removing hidden files
    dir1_extra_files = [files_map[x] for x in dir1_extra_files if not x.startswith('.')]
    dir2_extra_files = [files_map[x] for x in dir2_extra_files if not x.startswith('.')]

    print(f'Dir1 extra files {dir1_extra_files}')
    print(f'Dir1 less files {dir2_extra_files}')
    print('====================')
    print(f'Dir2 extra files {dir2_extra_files}')
    print(f'Dir2 less files {dir1_extra_files}')


files_map = {}


def read_directory(directory):
    dir_files = os.listdir(directory)

    files = []

    for obj in dir_files:
        obj_path = os.path.join(directory, obj)
        files_map[obj] = obj_path
        files.append(obj)

        is_dir = os.path.isdir(obj_path)

        if is_dir:
            files.extend(read_directory(obj_path))

    return set(files)


def pick_directory_1():
    global files_dir1
    dir_path = filedialog.askdirectory(mustexist=True)
    print(f'Dir1: {dir_path}')
    files_dir1 = read_directory(dir_path)


def pick_directory_2():
    global files_dir2
    dir_path = filedialog.askdirectory(mustexist=True)
    print(f'Dir2: {dir_path}')
    files_dir2 = read_directory(dir_path)


w = tk.Tk()
w.title('Folder Difference Checker')
button_folder1 = tk.Button(w, text='Pick Folder 1', width=35, command=pick_directory_1)
button_folder2 = tk.Button(w, text='Pick Folder 2', width=35, command=pick_directory_2)
button_check_diff = tk.Button(w, text='Check Difference', width=35, command=check_difference)

button_folder1.pack()
button_folder2.pack()
button_check_diff.pack()

w.mainloop()
