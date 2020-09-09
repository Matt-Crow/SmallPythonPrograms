from pathlib import Path
import os

IGNORE = (".git", ".gradle", "build", ".nb-gradle") # ignores any of these folders
ENTENSIONS = ("java", "js", "py", "c", "cpp") # only counts files with these extensions

def countFiles(pathStr):
    if str(pathStr).endswith(IGNORE):
        return 0

    pathObj = Path(pathStr)
    #print("Count files for " + str(pathObj))

    total = 0
    for fileOrDir in pathObj.iterdir():
        #print(fileOrDir)
        if fileOrDir.is_dir():
            total = total + countFiles(fileOrDir)
        elif str(fileOrDir).endswith(ENTENSIONS):
            total = total + 1
    print(str(pathObj) + " contains " + str(total) + " files")
    return total

if __name__ == "__main__":
    print("Enter a path to count classes for: ")
    path = input()
    print(countFiles(path))
