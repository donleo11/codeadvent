import math

import utils
from step import Step

# def getsegments(cordstring):
#     horizontal_list = list()
#     vertical_list = list()
#     x = 0
#     y = 0
#     for item in cordstring:
#         direction = str(item[0])
#         value = int(item[1:])
#         if direction == "R":
#             add_segment(x, x + value, y, horizontal_list)
#             x = x + value
#         elif direction == "L":
#             add_segment(x, x - value, y, horizontal_list)
#             x = x - value
#         elif direction == "U":
#             add_segment(y, y + value, x, vertical_list)
#             y = y + value
#         elif direction == "D":
#             add_segment(y, y - value, x, vertical_list)
#             y = y - value
#     return horizontal_list, vertical_list
#
#
# def getcoordinates(cordstring):
#     x_coordinates = list()
#     y_coordinates = list()
#     x = 0
#     y = 0
#     x_coordinates.append(0)
#     y_coordinates.append(0)
#     for item in cordstring:
#         direction = str(item[0])
#         value = int(item[1:])
#         if direction == "R":
#             x_coordinates.append(x + value)
#             y_coordinates.append(y)
#             x = x + value
#         elif direction == "L":
#             x_coordinates.append(x - value)
#             y_coordinates.append(y)
#             x = x - value
#         elif direction == "U":
#             y_coordinates.append(y + value)
#             x_coordinates.append(x)
#             y = y + value
#         elif direction == "D":
#             y_coordinates.append(y - value)
#             x_coordinates.append(x)
#     return x_coordinates, y_coordinates
#
#
# def add_segment(start, finish, y, segment_list):
#     segment_list.append(Step([start, finish], y))
#
#
# def getclosest_knot(points):
#     closest_distance = math.inf
#     for point in points:
#         distance = getmanhattan_distance(point)
#         if distance < closest_distance: closest_distance = distance
#     return closest_distance
#
#
# def getmanhattan_distance(point):
#     return abs(point[0]) + abs(point[1])
#
#
# def getmatchlist(horizontal_list, vertical_list):
#     matchlist = list()
#     for horizontal_segment in horizontal_list:
#         for vertical_segment in vertical_list:
#             if vertical_segment.in_range(horizontal_segment.value) and horizontal_segment.in_range(
#                     vertical_segment.value):
#                 matchlist.append([vertical_segment.value, horizontal_segment.value])
#     return matchlist
#
#
# def find_matches(cord1string, cord2string):
#     segmentlist1 = getsegments(cord1string)
#     segmentlist2 = getsegments(cord2string)
#
#     matches = getmatchlist(segmentlist1[0], segmentlist2[1])[1:]
#     matches.extend(getmatchlist(segmentlist2[0], segmentlist1[1][1:]))
#     return matches
#
#
# def calculate_steps(coordinates, point):
#     for i in range(len(coordinates)):
#         coordinate = coordinates[i]
from wire import Wire

stringlist = utils.getinput2("day3.txt")
wire1string = str(stringlist[0]).strip().split(",")
steps1 = utils.generatesteps(wire1string)
coordinates1 = utils.generatecoordinates(steps1)
wire2string = str(stringlist[1]).strip().split(",")
steps2 = utils.generatesteps(wire2string)
coordinates2 = utils.generatecoordinates(steps2)

wire1 = Wire(steps1, coordinates1)
wire2 = Wire(steps2, coordinates2)


# matches = find_matches(cord1string, cord2string)
# coordinates1 = getcoordinates(cord1string)
# coordinates2 = getcoordinates(cord2string)
#
# print("Coordinates 1: ", coordinates1)
# print("Coordinates 2: ", coordinates2)

# looks into what knot is the closest to everything

# Need to find what is the closest in the amount of steps, rather than the Manhatten distance
