import read_utils
import utils
from mypoint import MyPoint

# get content
stringlist = read_utils.getinput2("day3.txt")
wire1string = str(stringlist[0]).strip().split(",")
wire2string = str(stringlist[1]).strip().split(",")

# generate segments
segments1 = utils.generatesegments(wire1string)
segments2 = utils.generatesegments(wire2string)

# find intersections
intersections = utils.find_intersects(segments1, segments2)
intersections.extend(utils.find_intersects(segments2, segments1))
intersections = utils.remove_duplicates(intersections)

# find closest point
closest_point: MyPoint = utils.getclosest_point(intersections[1:])

# Answer question A
print("Question A: " + str(utils.getmanhattan_distance(closest_point)))







