import read_utils
from day3 import segment_utils
from day3.mypoint import MyPoint

# get content
stringlist = read_utils.getinput2("day3.txt")
wire1string = str(stringlist[0]).strip().split(",")
wire2string = str(stringlist[1]).strip().split(",")

# generate segments
segments1 = segment_utils.generatesegments(wire1string)
segments2 = segment_utils.generatesegments(wire2string)

# find intersections
intersections = segment_utils.find_intersects(segments1, segments2)
intersections.extend(segment_utils.find_intersects(segments2, segments1))
intersections = segment_utils.remove_duplicates(intersections)

# Question A specific
# find closest point
closest_point: MyPoint = segment_utils.getclosest_point(intersections[1:])

# Answer question A
print("Question A: " + str(segment_utils.getmanhattan_distance(closest_point)))

# Question B specific
count: int = segment_utils.find_closest_step(segments1, segments2, intersections[1:])
print("Question B: " + str(count))






