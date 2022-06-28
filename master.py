import sys


def execution(count):
    exec(open("./slave.py").read(), {'k': count})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execution(int(sys.argv[1]))
    else:
        execution(500)