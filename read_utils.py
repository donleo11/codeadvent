def getinput(filename):
    with open(filename, "r") as f:
        linelist = f.readlines()

    cleanlist = list()
    for line in linelist:
        cleanlist.append(line.strip())
    return cleanlist


def getinput2(filename):
    with open(filename, "r") as f:
        linelist = f.readlines()
    return linelist

def converttofloat(stringlist):
    floatlist = list()
    for line in stringlist:
        floatlist.append(float(line))
    return floatlist


def converttoint(stringlist):
    intlist = list()
    for line in stringlist:
        intlist.append(int(line))
    return intlist
