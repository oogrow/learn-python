"""File Name: 批量修改文件名字
   Python   : Python 3.7.0b3

   批量修改path目录下的文件名
"""

# -*- coding: utf-8 -*-
import os

def rename_file(path):
    files = os.listdir(path)
    for f in files:
        oldname = path + f

        # 批量修改文件名字，用数字命名，数字递增
        # '%02d'%files.index(f) 使用files列表下标并用两位作为名字
        # 暂时没有找到可以根据文件总数对应的位数来作为名字长度
        newname = path + '%02d'%files.index(f) + '.' + f.split('.')[-1]
        os.rename(oldname, newname)

if __name__ == '__main__':
    # path 是进行文件修改名字的主目录
    path = 'C:/Users/Username/Desktop/picture/'
    rename_file(path)