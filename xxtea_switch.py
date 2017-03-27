#!/usr/bin/python3
# coding=utf-8

# 使用 xxtea 算法加解密文件的工具, 仅单个文件
# 例子: 
# 加密:
# python xxtea_switch.py -m e -k key -s sign -i inputfile -o outputfile
# 
# 解密:
# python xxtea_switch.py -m d -k key -s sign -i inputfile -o outputfile

import sys
import getopt
from utils_3rd.xxtea import encrypt
from utils_3rd.xxtea import decrypt

mode = None
key = None
sign = None
inputFile = None
outputFile = None

def findOptValue(optlist, opt):
    for v in (optlist):
        if v[0] == opt:
            return v[1]
    return None

if __name__ == "__main__":
    optlist, args = getopt.getopt(sys.argv[1:], "m:k:s:i:o:")
    print(optlist)
    mode = findOptValue(optlist, "-m")
    key = findOptValue(optlist, "-k")
    sign = findOptValue(optlist, "-s")
    inputFile = findOptValue(optlist, "-i")
    outputFile = findOptValue(optlist, "-o")

    if mode == None:
        print("请输入模式 e/d")
        sys.exit()

    if key == None:
        print("请输入 key")
        sys.exit()

    if sign == None:
        print("请输入 sign")
        sys.exit()

    if inputFile == None:
        print("请输入 input file")
        sys.exit()

    if outputFile == None:
        print("请输入 output file")
        sys.exit()

    file = open(inputFile, "rb")
    rawdata = file.read()
    file.close()

    if mode == "e":
        rawdata = encrypt(rawdata, key)
        rawdata = sign + rawdata
    else:
        rawdata = rawdata[len(sign):]
        rawdata = decrypt(rawdata, key)

    file = open(outputFile, "wb")
    file.write(rawdata)
    file.close()

