import sys

def template(x, y, z):
    return "%s時の%sは%s" % (x, y, z)

def main():
    x, y, z = 12, "TEMP", 22.4
    print(template(x, y, z))

if __name__ == '__main__':
    main()
    