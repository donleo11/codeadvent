import math

from constants import Constants
from day3.mypoint import MyPoint
from day3.segment import Segment


def generatesegments(string_list):
    segment_list = list()
    firstpoint: MyPoint = MyPoint(0, 0)
    for segment_string in string_list:
        segment = Segment(segment_string[0], int(segment_string[1:]), firstpoint)
        segment_list.append(segment)
        firstpoint = segment.getsecondpoint()
    return segment_list


def segment_intersection(segment1: Segment, segment2: Segment):
    if inxrange(segment1, segment2) and inyrange(segment1, segment2):
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


def inrange(segment1: Segment, segment2: Segment):
    if segment1.ishorizontal() and segment2.ishorizontal() or segment1.isvertical() and segment2.isvertical():
        return False
    else:
        horizontal_segment: Segment = segment1 if segment1.ishorizontal() else segment2
        vertical_segment: Segment = segment1 if segment1.isvertical() else segment2
        return inxrange(horizontal_segment, vertical_segment) and inyrange(horizontal_segment, vertical_segment)


def inxrange(horizontal_segment: Segment, vertical_segment: Segment):
    if horizontal_segment.direction == Constants.right:
        return horizontal_segment.firstpoint.x <= vertical_segment.firstpoint.x <= horizontal_segment.getsecondpoint().x
    else:
        return horizontal_segment.getsecondpoint().x <= vertical_segment.firstpoint.x <= horizontal_segment.firstpoint.x


def inyrange(horizontal_segment: Segment, vertical_segment: Segment):
    if vertical_segment.direction == Constants.up:
        return vertical_segment.firstpoint.y <= horizontal_segment.firstpoint.y <= vertical_segment.getsecondpoint().y
    else:
        return vertical_segment.getsecondpoint().y <= horizontal_segment.firstpoint.y <= vertical_segment.firstpoint.y


def getclosest_point(points):
    closest_distance = math.inf
    closest_point: MyPoint
    for point in points:
        distance = getmanhattan_distance(point)
        if distance < closest_distance:
            closest_distance = distance
            closest_point = point
    return closest_point


def getmanhattan_distance(point: MyPoint):
    return abs(point.x) + abs(point.y)


def remove_duplicates(the_list):
    res = list()
    for i in the_list:
        if i not in res:
            res.append(i)
    return res


def find_intersects(segments1, segments2):
    intersections = list()
    for segment1 in segments1:
        for segment2 in segments2:
            if segment1.ishorizontal() and segment2.isvertical() or segment1.isvertical() and segment2.ishorizontal():
                intersect = segment_intersection(segment1, segment2)
                if intersect:
                    intersections.append(intersect)
    return intersections


def distance(a: MyPoint, b: MyPoint):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def is_between(a: MyPoint, c: MyPoint, b: MyPoint):
    return distance(a, c) + distance(c, b) == distance(a, b)


def count_steps(segments, point: MyPoint):
    count: int = 0
    for segment in segments:
        if not is_between(segment.firstpoint, point, segment.getsecondpoint()):
            count = count + segment.length
        else:
            if segment.ishorizontal():
                return count + abs(segment.firstpoint.x - point.x)
            else:
                return count + abs(segment.firstpoint.y - point.y)
    return count


def find_closest_step(segments1, segments2, intersections):
    count = math.inf
    for intersect in intersections:
        count1: int = count_steps(segments1, intersect)
        count2: int = count_steps(segments2, intersect)
        if count1 + count2 < count: count = count1 + count2
    return count
