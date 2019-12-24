# get content
import orbit_utils
import read_utils
from orbit import Orbit

stringlist = read_utils.getinput2("day6.txt")
orbits = list()
for item in stringlist:
    items = item.strip().split(")")
    orbits.append(Orbit(items[0], items[1]))

count = orbit_utils.count_orbits(orbits)
print("Total orbits: ", count)
