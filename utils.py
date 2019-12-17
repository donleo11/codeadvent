from mypoint import MyPoint
from step import Step


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


def generatesteps(string_list):
    step_list = list()
    for step in string_list:
        step_list.append(Step(step[0], int(step[1:])))
    return step_list


def generatecoordinates(steps):
    coordinates = list()
    coordinates.append(MyPoint(0, 0))
    last_point = coordinates[0]
    for step in steps:
        coordinates.append(getnextpoint(step, last_point))
    return coordinates


def getnextpoint(step: Step, oldpoint: MyPoint):
    if step.direction == 'R':
        return MyPoint(oldpoint.x + step.length, oldpoint.y)
    elif step.direction == 'L':
        return MyPoint(oldpoint.x - step.length, oldpoint.y)
    elif step.direction == 'U':
        return MyPoint(oldpoint.x, oldpoint.y + step.length)
    elif step.direction == "D":
        return MyPoint(oldpoint.x, oldpoint.y - step.length)

    def next_point(self):
        nextx = 0
        nexty = 0
        if self.direction == "R":
            nextx = self.x + self.value
            nexty = self.y
        elif self.direction == "L":
            nextx = self.x - self.value
            nexty = self.y
        elif self.direction == "U":
            nexty = self.y + self.value
            nextx = self.x
        elif self.direction == "D":
            nexty = self.y - self.value
            nextx = self.x
        return [nextx, nexty]
