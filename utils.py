from mypoint import MyPoint
from segment import Segment


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


def generatesegments(string_list):
    segment_list = list()
    firstpoint: MyPoint = MyPoint(0, 0)
    for segment_string in string_list:
        segment = Segment(segment_string[0], int(segment_string[1:]), firstpoint)
        segment_list.append(segment)
        firstpoint = segment.getsecondpoint()
    return segment_list


def segment_intersection(segment1: Segment, segment2: Segment):
    if segment1.inxrange(segment2) and segment1.inyrange(segment2):
        return line_intersection(segment1, segment2)
    else:
        return False


def line_intersection(segment1: Segment, segment2: Segment):
    xdiff: MyPoint = MyPoint(segment1.firstpoint.x - segment1.getsecondpoint().x,
                             segment2.firstpoint.x - segment2.getsecondpoint().x)
    ydiff: MyPoint = MyPoint(segment1.firstpoint.y - segment1.getsecondpoint().y,
                             segment2.firstpoint.y - segment2.getsecondpoint().y)

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d: MyPoint = MyPoint(det(segment1.firstpoint, segment1.getsecondpoint()),
                         det(segment2.firstpoint, segment2.getsecondpoint()))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return MyPoint(x, y)


def det(a: MyPoint, b: MyPoint):
    return a.x * b.y - a.y * b.x

# def findintersect(wire1: Wire, wire2: Wire):
#     for i in range(len(wire1.steps)):
#         for j in range(len(wire2.steps)):
#
#         wirepoint: MyPoint = wire.coordinates[i]
#         step: Step = wire.steps[i]
#         if (step.direction == Constants.right or step.direction == Constants.left) and wirepoint.y == point.y:
#             if step.direction == Constants.right and wirepoint.x < point.x < step.length + wirepoint.x:
#                 return MyPoint(point.x, )
