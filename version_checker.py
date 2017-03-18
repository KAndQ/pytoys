#!/usr/bin/python3

import json
import sys

def readFile(path):
    rawdata = ""
    try:
        file = open(path)
        rawdata = file.read()
        file.close()
    except BaseException as e:
        print(e)
    finally:
        return rawdata

NEW_FILE = "./version_info_new.json"
OLD_FILE = "./version_info_old.json"

if __name__ == "__main__":
    v1rawdata = readFile(NEW_FILE)
    v2rawdata = readFile(OLD_FILE)

    if v1rawdata == "" or v2rawdata == "":
        sys.exit()

    v1data = json.loads(v1rawdata)
    v2data = json.loads(v2rawdata)
    
    print("compare v1 = %s, v2 = %s" % (v1data["appversion"], v2data["appversion"]))
    diffFiles = []

    v1files = v1data["files"]
    v2files = v2data["files"]
    for k, v1 in v1files.items():
        if k in v2files:
            v2 = v2files[k]
            if v1["code"] != v2["code"]:
                diffFiles.append(v1)
        else:
            diffFiles.append(v1)

    sumSize = 0.0
    outputFile = open("./details.txt", "w")
    outputFile.write("diff files: \n")
    for v in diffFiles:
        sumSize += int(v["bytes"])
        outputFile.write("\t" + v["name"] + "\n")

    outputFile.write("================================================================================\n")
    outputFile.write("sum size: %.4fMB\n" % (sumSize / 1024 / 1024))
    outputFile.close()

    print("Compare done. Please check details.txt file.")
