import sys


try:
    name = (sys.argv)
    for i in range(len(name)):
        print(sys.argv[i + 1])
except BaseException:
    print("no args")