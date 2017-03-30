#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MD5 校验工具
# 输入一个文件名是获得该文件的 MD5 值;
# 输入两个文件名是比对两个文件的 MD5 值是否相同;

import sys, os
from os import path
import hashlib

def getFileMD5(file):
    try:
        f = open(file, "rb")
        f.seek(0, 0)
        f.seek(0, 2)
        endPos = f.tell()
        f.seek(0, 0)

        m = hashlib.md5()
        while True:
            data = f.read(1024)
            m.update(data)
            if f.tell() == endPos:
                break
        return m.hexdigest()
    except BaseException as e:
        print(e)
    finally:
        f.close()

def compareFile(file1, file2):
    file1Md5 = getFileMD5(file1)
    file2Md5 = getFileMD5(file2)
    return file1Md5 == file2Md5, file1Md5, file2Md5

if __name__ == "__main__":
    if len(sys.argv) == 3:
        result, file1Md5, file2Md5 = compareFile(sys.argv[1], sys.argv[2])
        if result:
            print("same md5 = %s" % (file1Md5))
        else:
            name1 = path.basename(sys.argv[1])
            name2 = path.basename(sys.argv[2])
            print("different:\n%s = %s\n%s = %s" % (name1, file1Md5, name2, file2Md5))
    else:
        fileMd5 = getFileMD5(sys.argv[1])
        print("md5 = %s" % fileMd5)


