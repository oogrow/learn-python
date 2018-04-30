"""File Name: 按文件类型分类文件
   Python   : Python 3.7.0b3

   对path目录下的文件按文件类型分类，把不同文件类型放至相对应的子文件夹中
"""

# -*- coding: utf-8 -*-
import os
import shutil

def sort_file(path):
    files = os.listdir(path)
    for f in files:
        folder_path_name = path + f.split('.')[-1]
        file_path_name = path + f
        if not os.path.exists(folder_path_name):
            os.makedirs(folder_path_name)
            # 如果没有该文件类型对应的文件夹，就新建一个以该文件类型为名的子文件夹
            shutil.move(file_path_name, folder_path_name)
        else:
            shutil.move(file_path_name, folder_path_name)

if __name__ == '__main__':
    # path 是进行文件分类的主目录
    path = '/Users/Username/Desktop/sort_file/'
    sort_file(path)